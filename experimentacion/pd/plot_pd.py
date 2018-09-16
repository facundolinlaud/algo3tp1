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

		for cardinal, str_measures in run_results.items():
			masked_measures = []
			masked_ticks = []
			masked_recursiones = []
			masked_Ts = []

			for m in str_measures:
				masked_measures.append(float(m['segundos']))
				masked_ticks.append(int(m['ticks']))
				masked_recursiones.append(int(m['recursiones']))
				masked_Ts.append(int(m['T']))

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
			plot_runs[run_name][cardinal]['all_measures'] = measures
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

	# pdb.set_trace()
	############################ prog din ##############################
	prodin = 'Prog. Din.'
	yss = []
	xs = [int(i) for i in runs[prodin].keys()]
	ys = []
	yerror = []

	for stats in runs[prodin].values():
		ys.append(stats['mean'])
		yss.append(stats['all_measures'])
		yerror.append(stats['stdev'])

	# xs, ys, yerror = (list(t) for t in zip(*sorted(zip(xs, ys, yerror)))) # sorts xs, ys and yerror by xs

	xs = [int(i) for i in xs]
	ys = [float(i) for i in ys]
	yerror = [float(i) for i in yerror]

	lines[prodin] = {}
	lines[prodin]['xs'] = xs
	lines[prodin]['yss'] = yss
	lines[prodin]['ys'] = ys
	lines[prodin]['yerror'] = yerror

	######################### prog din lin aprox #########################
	lines['lineal_aprox'] = get_linear_aprox(xs, ys)

	######################### complejidad ###############################
	cota_xs = []#runs[prodin].keys()
	cota_ys = []

	segundos = []
	recursiones = []

	for cardinal, stats in runs[prodin].items():
		segundos.append(stats['mean'])
		recursiones.append(stats['mean_recursiones'])

	Os_de_1 = np.divide(segundos, recursiones)
	O_de_1 = statistics.mean(Os_de_1)

	for cardinal, stats in runs[prodin].items():
		cota_xs.append(cardinal)
		cota_ys.append(cardinal * stats['mean_Ts'] * O_de_1)

	lines['cota'] = {}
	lines['cota']['xs'] = cota_xs
	lines['cota']['ys'] = cota_ys

	######################## complejidad lin aprox #########################
	lines['cota_linear_aprox'] = get_linear_aprox(cota_xs, cota_ys)
	return lines

def get_linear_aprox(xs, ys):
	# pdb.set_trace()
	A = np.vstack([xs, np.ones(len(xs))]).T
	m, c = np.linalg.lstsq(A, ys)[0]
	return {
		'A' : A,
		'm' : m,
		'c' : c
	}

def plot(lines):
	log('plotting', 0)
	
	## scaling y limites de los ejes
	# plt.yscale('log', basey=10)
	# plt.xscale('log', basex=2)

	## setup
	run_name = 'Prog. Din.'
	line = lines[run_name]

	########## scatter ##########
	plt.scatter([], [], c='g', label='Programación Dinámica')

	for xe, ye in zip(line['xs'], line['yss']):
		s=[np.sqrt(i) for i in line['xs']]
		plt.scatter([xe] * len(ye), ye, c="g", alpha=0.15, s=20)

	##################
	# plt.errorbar(line['xs'], line['ys'], yerr=line['yerror'], label='Programación Dinámica', color=resolve_color(run_name), 
	# 	linewidth=1, xerr=None, fmt='o-', ecolor=None, elinewidth=1, capsize=1, barsabove=False, lolims=False, 
	# 	uplims=False, xlolims=False, xuplims=False, errorevery=2, capthick=1, hold=None, data=None, markersize=2)

	cota = lines['cota']
	plt.errorbar(cota['xs'], cota['ys'], label='Cota superior', color='C3', linewidth=1, xerr=None, fmt='o-',
	ecolor=None, elinewidth=1, capsize=1, barsabove=False, lolims=False, uplims=False, xlolims=False, 
	xuplims=False, errorevery=1, capthick=0.5, hold=None, data=None, markersize=3)

	#m = lines['lineal_aprox']['m']
	#c = lines['lineal_aprox']['c']
	#start_line_x = line['xs'][0]
	#end_line_x = line['xs'][-1]
	#x = np.linspace(start_line_x, end_line_x, 1000)
	#plt.plot(x, m*x + c, 'r', linestyle='-', linewidth=1, color='g')
#
#	#x2 = np.linspace(18, end_line_x, 1000)
#	#cota_m = lines['cota_linear_aprox']['m']
#	#cota_c = lines['cota_linear_aprox']['c']
#	#plt.plot(x2, cota_m*x2 + cota_c, 'r', linestyle='-', linewidth=1, color='r')
	##############

	# plt.errorbar(line['xs'], line['ys'], yerr=line['yerror'], label=run_name, color=resolve_color(run_name), linewidth=1, xerr=None, fmt='o-', ecolor=None, elinewidth=1, capsize=1, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=0.5, hold=None, data=None, markersize=3)

	## labels
	#plt.suptitle('Ondas', fontsize=16)
	#plt.title('Ciclos consumidos por píxel en función de píxeles totales\ncon desviación estándar')
	plt.xlabel('n')
	plt.ylabel('Tiempo (milésimas)')
	plt.legend()
	plt.ticklabel_format(style='sci', axis='y')
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
		'' : 'C4',	# purpura
		'Back-Tracking' : 'C0',	# azul
		'Prog. Din.' : 'C2',	# verde
		'O2' : 'C1',	# dorado
		'Brute-Force' : 'C3'		# rojo
	}

	if run_name in colors.keys():
		return colors[run_name]
	return None

## start 
default_raw_input = 'out_asm_ondas_by_ondas.txt'
using_this_raw_input = default_raw_input if len(argv) == 1 else argv[-1]
log('cargando de ' + using_this_raw_input, 0)
main(using_this_raw_input)
