# usage: python3 measure.py params_file.py output_file.txt

# imports
from sys import argv
import subprocess
import pdb
import random

def main(params, output_file):
	log('starting', 0)
	results_per_exec = {}
	problems = build_problems(params)

	for run_name, run_desc in params['runs'].items():
		log('exec %s' % run_name, 1)
		results_per_exec[run_name] = run_for_algorithm(params, run_desc['algorithm'], problems)
	
	save_to_file(output_file, results_per_exec)
	return

def run_for_algorithm(params, algorithm, problems):
	results_per_T = {}

	i = start = params['T_start']
	end = params['T_end']
	multiplier = params['T_multiplier']

	while i < end:
		log('T = %i' % i, 2)
		results_per_T[i] = []

		for r in range(0, params['repetitions_per_n']):
			log('repetition %i' % r, 3)
			result = execute(params['exe'], algorithm, problems[i][r], params['fixed_n'])
			results_per_T[i].append(result)

		i *= multiplier
	return results_per_T

MAX_VALUE = 99 # el maximo valor de un elemento en values
MIN_VALUE = 0 # el minimo valor de un elemento en values

def build_problems(params):
	i = start = params['T_start']
	end = params['T_end']
	multiplier = params['T_multiplier']
	problems = {}
	
	while i < end:
		problems[i] = []

		for r in range(0, params['repetitions_per_n']):
			problems[i].append(create_subset_problem_of_size(params['fixed_n'], params['include_unsolvable_problems'], 
				i, params['shuffle_problems'], params['solutions_at_tail']))

		i *= multiplier

	return problems

def create_subset_problem_of_size(n, include_unsolvable_problems, T, shuffle_problems, solutions_at_tail):
	with_solution = random.randint(0, 1) or not include_unsolvable_problems
	values = []
	result = {}

	if(with_solution):
		assured_solution_cardinal = random.randint(1, n)
		t_divided_by_assured_cardinal = int(T / assured_solution_cardinal)
		values += [t_divided_by_assured_cardinal] * (assured_solution_cardinal - 1)
		values.append(T - t_divided_by_assured_cardinal * (assured_solution_cardinal - 1))
		
		garbage_cardinal = n - assured_solution_cardinal

		for i in range(0, garbage_cardinal):
			garbage = random.randint(MIN_VALUE, MAX_VALUE)
			if solutions_at_tail:
				values.insert(0, garbage)
			else:
				values.append(garbage)

		if shuffle_problems:
			random.shuffle(values)

		result['T'] = T
		result['has_solution'] = True
	else:
		for i in range(0, n):
			probably_garbage_value = random.randint(MIN_VALUE, MAX_VALUE)
			values.append(probably_garbage_value)

		result['T'] = T
		result['has_solution'] = False

	result['values'] = values
	return result

def execute(exe, algorithm, problem, values_cardinal):
	command = [
		exe, 
		algorithm, 
		str(problem['T']), 
		str(values_cardinal)] + [str(i) for i in problem['values']]

	console_out = subprocess.run(command, stdout = subprocess.PIPE)
	return get_time(str(console_out.stdout), problem['T'], problem['has_solution'])

def get_time(console_out, T, solvable):
	lines = console_out.split('\\n')
	
	return {
		'resultado' : int(lines[2].split()[-1]),
		'recursiones' : int(lines[3].split()[-1]),
		'ticks' : float(lines[4].split()[-1]),
		'segundos' : float(lines[5].split()[-1]),
		'T' : T,
		'has_solution' : solvable,
		'seg2' : float(lines[6].split()[-1])
	}

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