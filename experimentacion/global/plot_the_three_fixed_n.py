## imports
import pdb
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sys import argv
import math


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

		for cardinal, str_measures in run_results.items():
			masked_measures = []
			masked_ticks = []
			masked_recursiones = []
			masked_Ts = []

			for m in str_measures:
				masked_measures.append(float(m['segundos']))
				masked_ticks.append(int(m['ticks']))
				masked_recursiones.append(float(m['recursiones']))
				masked_Ts.append(int(m['T']))

			# masked_measures = np.multiply(masked_measures, [1000] * len(masked_measures)) # segundos a milisegundos
			masked_measures = stats.mstats.trim(masked_measures, (0, 0), relative=True)

			measures = []
			ticks = []
			recursiones = []
			Ts = []

			measures = []
			for i, m in enumerate(masked_measures.tolist()):
				if m is not None:
					measures.append(m)
					ticks.append(masked_ticks[i])
					recursiones.append(masked_recursiones[i])
					Ts.append(masked_Ts[i])

			mean = statistics.mean(measures)
			plot_runs[run_name][cardinal] = {}
			plot_runs[run_name][cardinal]['mean'] = mean
			plot_runs[run_name][cardinal]['median'] = statistics.median(measures)
			plot_runs[run_name][cardinal]['stdev'] = statistics.stdev(measures)
			plot_runs[run_name][cardinal]['variance'] = statistics.variance(measures, mean)
			plot_runs[run_name][cardinal]['sterr'] = stats.sem(measures)
			# cosas super extra
			plot_runs[run_name][cardinal]['mean_ticks'] = statistics.mean(ticks)
			plot_runs[run_name][cardinal]['mean_recursiones'] = statistics.mean(recursiones)
			plot_runs[run_name][cardinal]['mean_Ts'] = statistics.mean(Ts)

	log('Parsed runs:', 0)
	print(plot_runs)
	
	return plot_runs

def preplot(runs):
	lines = {}

	for run_name in runs:
		xs = [int(i) for i in runs[run_name].keys()]
		ys = []
		yerror = []

		for stats in runs[run_name].values():
			ys.append(stats['mean'])
			yerror.append(stats['stdev'])

		# xs, ys, yerror = (list(t) for t in zip(*sorted(zip(xs, ys, yerror)))) # sorts xs, ys and yerror by xs

		xs = [int(i) for i in xs]
		ys = [float(i) for i in ys]
		yerror = [float(i) for i in yerror]

		lines[run_name] = {}
		lines[run_name]['xs'] = xs
		lines[run_name]['ys'] = ys
		lines[run_name]['yerror'] = yerror

	return lines

def plot(lines):
	log('plotting', 0)

	## scaling y limites de los ejes
	# plt.yscale('log', basey=2)
	plt.xscale('log', basex=10)

	## setup
	for run_name, line in lines.items():
		plt.errorbar(line['xs'], line['ys'], label=run_name, color=resolve_color(run_name), linewidth=1, xerr=None, fmt='o-', ecolor=None, elinewidth=1, capsize=1, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=0.5, hold=None, data=None, markersize=3)
		# plt.errorbar(line['xs'], line['ys'], yerr=line['yerror'], label=run_name, color=resolve_color(run_name), linewidth=1, xerr=None, fmt='o-', ecolor=None, elinewidth=1, capsize=1, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=0.5, hold=None, data=None, markersize=3)

	## labels
	#plt.suptitle('Ondas', fontsize=16)
	#plt.title('Ciclos consumidos por píxel en función de píxeles totales\ncon desviación estándar')
	plt.xlabel('T (valor objetivo)')
	plt.ylabel('Tiempo (segundos)')
	plt.legend()
	#plt.legend(loc='upper right', bbox_to_anchor=(0.99, 0.8)) # para que no tape la linea de O0

	## grids
	plt.grid(True)
	plt.grid(b=True, which='major', color='black', linestyle='dotted', alpha=0.3)
	plt.grid(b=True, which='minor', color='black', linestyle='dotted', alpha=0.05)
	plt.minorticks_on()

	# xs = line['xs']
	# xint = range(min(xs), math.ceil(max(xs))+1, 3)
	# plt.xticks(xint)

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
		'Back-Tracking' : 'C0',	# azul
		'Prog. Din.' : 'C2',	# verde
		'Brute-Force' : 'mediumpurple'		# purpura
	}

	if run_name in colors.keys():
		return colors[run_name]
	return None

## start 
default_raw_input = 'out_asm_ondas_by_ondas.txt'
using_this_raw_input = default_raw_input if len(argv) == 1 else argv[-1]
log('cargando de ' + using_this_raw_input, 0)
main(using_this_raw_input)
