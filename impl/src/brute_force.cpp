//
// Created by Facundo Linlaud on 5/9/18.
//

#include "brute_force.h"

brute_force::brute_force(int _values[], int _n) : values(_values), n(_n){}

bool brute_force::is_subset_solution(int k_left, int from, int t){
    computations ++;

    if(k_left == 0) {
        if (t == 0) {
            return true;
        } else {
            return false;
        }
    } else {
        if(k_left == n - from){
            return is_subset_solution(k_left - 1, from + 1, t - values[from]);
        }else{
            return is_subset_solution(k_left - 1, from + 1, t - values[from]) or
                    is_subset_solution(k_left, from + 1, t);
        }
    }
}

int brute_force::calculate(int t){
    if(t == 0)
        return 0;

    int i = 0;

    while(!is_subset_solution(i, 0, t) and i <= n){
        i++;
    }

    return i < n ? i : INFINITY;
}