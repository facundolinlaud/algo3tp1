{
	'exe' : '../impl/cmake-build-debug/impl',
	'n_start' : 10,
	'n_end' : 30,
	'n_step' : 1,
	'repetitions_per_n' : 40,
	'include_unsolvable_problems' : True,
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
