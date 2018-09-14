//
// Created by Facundo Linlaud on 5/9/18.
//

#ifndef IMPL_BRUTE_FORCE_H
#define IMPL_BRUTE_FORCE_H

class brute_force {
    const long INFINITY = 999999;

private:
    int* values;
    int n;

    bool is_subset_solution(int k_left, int from, int t);

public:
    int computations;

    brute_force(int values[], int _n);

    int calculate(int t);

};


#endif //IMPL_BRUTE_FORCE_H
