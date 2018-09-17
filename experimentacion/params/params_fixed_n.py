{
	'exe' : '../impl/cmake-build-debug/impl',
	'T_start' : 10,
	'T_end' : 100000000,
	'T_multiplier' : 10,
	'repetitions_per_n' : 5,
	'fixed_n': 28,
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
		},
	}
}
