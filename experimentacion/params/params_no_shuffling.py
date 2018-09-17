{
	'exe' : '../impl/cmake-build-debug/impl',
	'n_start' : 10,
	'n_end' : 20,
	'n_step' : 1,
	'repetitions_per_n' : 2,
	'include_unsolvable_problems' : False,
	'shuffle_problems' : False,
	'solutions_at_tail' : True,
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
