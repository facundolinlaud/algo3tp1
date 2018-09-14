## imports
import pdb
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sys import argv


def main(raw_input):
	log('parsing raw results', 0)
	raw_runs = read_file(raw_input)
	runs_stats = do_statistics(raw_runs)
	plotable_runs = preplot(runs_stats)
	plot(plotable_runs)

def do_statistics(raw_input):
	plot_runs = {}

	for run_name, run_results in raw_input.items():
		plot_runs[run_name] = {}

		for size, str_measures in run_results.items():
			masked_measures = [int(i) for i in str_measures]
			masked_measures = stats.mstats.trim(masked_measures, (0.15, 0.15), relative=True)
			measures = []

			for m in masked_measures.tolist():
				if m is not None:
					measures.append(m)

			mean = statistics.mean(measures)
	
			plot_runs[run_name][size] = {}
			plot_runs[run_name][size]['mean'] = mean
			plot_runs[run_name][size]['median'] = statistics.median(measures)
			plot_runs[run_name][size]['stdev'] = statistics.stdev(measures)
			plot_runs[run_name][size]['variance'] = statistics.variance(measures, mean)
			plot_runs[run_name][size]['sterr'] = stats.sem(measures)

	log('Parsed runs:', 0)
	print(plot_runs)
	
	return plot_runs

def preplot(runs):
	lines = {}

	# pdb.set_trace()
	for run_name in runs:
		xs = []
		ys = []
		yerror = []

		for dimension in runs[run_name].keys():
			xy = dimension.split('x')
			x = int(xy[0])
			y = int(xy[1])
			xs.append(x * y)

		for stats in runs[run_name].values():
			ys.append(stats['mean'])
			yerror.append(stats['stdev'])

		xs, ys, yerror = (list(t) for t in zip(*sorted(zip(xs, ys, yerror)))) # sorts xs, ys and yerror by xs

		xs = [int(i) for i in xs]
		ys = [int(i) for i in ys]
		yerror = [int(i) for i in yerror]

		lines[run_name] = {}
		lines[run_name]['xs'] = xs
		lines[run_name]['ys'] = ys
		lines[run_name]['yerror'] = yerror

		#xs = pixels
		#ys = ciclos
		for index in range(0, len(lines[run_name]['ys'])):
			lines[run_name]['ys'][index] /= lines[run_name]['xs'][index]
			lines[run_name]['yerror'][index] /= lines[run_name]['xs'][index]

	return lines

def plot(lines):
	log('plotting', 0)
	
	## scaling y limites de los ejes
	#plt.yscale('log', basey=2)
	plt.xscale('log', basex=2)

	## setup
	for run_name, line in lines.items():
		plt.errorbar(line['xs'], line['ys'], yerr=line['yerror'], label=run_name, color=resolve_color(run_name), linewidth=1, xerr=None, fmt='o-', ecolor=None, elinewidth=1, capsize=1, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=0.5, hold=None, data=None, markersize=3)

	## labels
	#plt.suptitle('Ondas', fontsize=16)
	#plt.title('Ciclos consumidos por píxel en función de píxeles totales\ncon desviación estándar')
	plt.xlabel('# pixeles')
	plt.ylabel('# ciclos/pixeles')
	plt.legend()
	#plt.legend(loc='upper right', bbox_to_anchor=(0.99, 0.8)) # para que no tape la linea de O0

	## grids
	plt.grid(True)
	plt.grid(b=True, which='major', color='black', linestyle='dotted', alpha=0.3)
	plt.grid(b=True, which='minor', color='black', linestyle='dotted', alpha=0.05)
	plt.minorticks_on()

	plt.draw()
	plt.show()
	return

## codigo repetido porque python no te deja hacer las cosas bien
import ast

def log(text, level):
	print('=' * (len(text) + 2 * level))
	print(('..' * level) + text)

def read_file(file_name):
	log('reading from file', 0)

	file = open(file_name, 'r') 
	str = file.read()

	return ast.literal_eval(str)

def resolve_color(run_name):
	colors = {
		'ASM' : 'C4',	# purpura
		'O0' : 'C0',	# azul
		'O1' : 'C2',	# verde
		'O2' : 'C1',	# dorado
		'O3' : 'C3'		# rojo
	}

	if run_name in colors.keys():
		return colors[run_name]
	return None

## start 
default_raw_input = 'out_asm_ondas_by_ondas.txt'
using_this_raw_input = default_raw_input if len(argv) == 1 else argv[-1]
log('cargando de ' + using_this_raw_input, 0)
main(using_this_raw_input)
