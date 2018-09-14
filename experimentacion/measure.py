# usage: python3 measure.py params_file.py output_file.txt

# imports
from sys import argv
import subprocess
import pdb
import random

def main(params, output_file):
	log('starting', 0)
	results_per_exec = {}

	for run_name, run_desc in params['runs'].items():
		log('exec %s' % run_name, 1)
		results_per_exec[run_name] = run_for_algorithm(params, run_desc['algorithm'])
	
	save_to_file(output_file, results_per_exec)
	return

def run_for_algorithm(params, algorithm):
	results_per_n = {}

	for i in range(params['n_start'], params['n_end'], params['n_step']):
		log('n = %i' % i, 2)
		results_per_n[i] = []

		for r in range(0, params['repetitions_per_n']):
			log('repetition %i' % r, 3)
			problem = create_subset_problem_of_size(i, params['include_unsolvable_problems'])
			result = execute(params['exe'], algorithm, problem, i)
			results_per_n[i].append(result)

	return results_per_n

def create_subset_problem_of_size(n, include_unsolvable_problems):
	MAX_VALUE = 99 # el maximo valor de un elemento en values
	MIN_VALUE = 0 # el minimo valor de un elemento en values

	with_solution = random.randint(0, 1)

	values = []
	result = {}

	if(with_solution and include_unsolvable_problems):
		assured_solution_cardinal = random.randint(1, n)
		T = 0
		
		for i in range(0, assured_solution_cardinal):
			solution_element = random.randint(MIN_VALUE, MAX_VALUE)
			values.append(solution_element)
			T += solution_element

		garbage_cardinal = n - assured_solution_cardinal

		for i in range(0, garbage_cardinal):
			garbage = random.randint(MIN_VALUE, MAX_VALUE)
			values.append(garbage)

		random.shuffle(values)

		result['T'] = T
	else:
		for i in range(0, n):
			probably_garbage_value = random.randint(MIN_VALUE, MAX_VALUE)
			values.append(probably_garbage_value)

		result['T'] = random.randint(0, MAX_VALUE * 2 * n)

	result['values'] = values
	return result

def execute(exe, algorithm, problem, values_cardinal):
	command = [
		exe, 
		algorithm, 
		str(problem['T']), 
		str(values_cardinal)] + [str(i) for i in problem['values']]

	console_out = subprocess.run(command, stdout = subprocess.PIPE)
	return get_time(str(console_out.stdout))

def get_time(console_out):
	lines = console_out.split('\\n')
	lines_of_interest = [i for i, s in enumerate(lines) if 'Segundos' in s]

	if(len(lines_of_interest) == 0):
		log('error leyendo output de consola. iniciando debug:', 4)
		pdb.set_trace()

	line_of_interest = lines_of_interest[0]

	return lines[line_of_interest].split()[-1]

def save_to_file(file_name, results):
	log('saving to file', 0)

	file = open(file_name, 'w')
	file.write(str(results))
	file.close()

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

## start
if len(argv) == 3:
	params_file = argv[1]
	save_file = argv[2]

	log('parametros de ' + params_file, 0)
	log('a guardar en ' + save_file, 0)

	main(read_file(params_file), save_file)
else:
	log('usage: python3 measure.py params_file.py output_file.txt', 0)