//
// Created by Facundo Linlaud on 5/9/18.
//

#ifndef IMPL_BRUTE_FORCE_H
#define IMPL_BRUTE_FORCE_H

class brute_force {
    const int ZERO = 0;
    const int NO_ELEMENT = -1;
    const int INFINITY = 999;

private:
    bool already_found;
    int* values;
    int n;

    bool best_partition(int k_left, int from, int t);

public:
    int computations;

    brute_force(int values[], int _n);

    int calculate(int t);

};


#endif //IMPL_BRUTE_FORCE_H
