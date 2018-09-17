{
	'exe' : '../impl/cmake-build-debug/impl',
	'T_start' : 10,
	'T_end' : 10000000000,
	'T_multiplier' : 10,
	'repetitions_per_n' : 2,
	'fixed_n': 10,
	'include_unsolvable_problems' : False,
	'shuffle_problems' : True,
	'solutions_at_tail' : False,
	'runs' : {
		'Brute-Force' : {
			'algorithm' : 'bf'
		},'Back-Tracking' : {
			'algorithm' : 'bt'
		},'Prog. Din.' : {
			'algorithm' : 'dp'
		}
	}
}
