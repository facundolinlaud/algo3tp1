//
// Created by Facundo Linlaud on 5/9/18.
//

#include <iostream>
#include "brute_force.h"

brute_force::brute_force(int _values[], int _n) : values(_values), n(_n), already_found(false){}

bool brute_force::best_partition(int k_left, int from, int t){
    if(already_found)
        return false;

    computations ++;

    if(k_left == 0) {
        if (t == 0) {
            already_found = true;
            return true;
        } else {
            return false;
        }
    } else {
        if(k_left == n - from){
            std::cout << "k_left == t - from" << std::endl;
            return best_partition(k_left - 1, from + 1, t - values[from]);
        }else{
            return best_partition(k_left, from + 1, t) or
                   best_partition(k_left - 1, from + 1, t - values[from]);
        }
    }
}

int brute_force::calculate(int t){
    already_found = false;
    int i = 0;

    while(!best_partition(i, 0, t) and i < n){
        i++;
    }

    return i;
}