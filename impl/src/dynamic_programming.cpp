//
// Created by Facundo Linlaud on 5/9/18.
//

#include <iostream>
#include "utils.h"
#include "dynamic_programming.h"

dynamic_programming::dynamic_programming(){}

int dynamic_programming::calculate(int n, int t, int values[n]){
    initialize_dic(n, t);
    int minimum_cardinal = subset_sum(values, n - 1, t);
    destroy_dic(n);

    return minimum_cardinal;
}

void dynamic_programming::initialize_dic(int n, int t){
    dic = new int*[n + 1];

    for(int i = 0; i <= n; i++){
        dic[i] = new int[t + 1];

        for(int accumulator = 0; accumulator <= t; accumulator++){
            dic[i][accumulator] = -1;
        }
    }
}

int dynamic_programming::subset_sum(int* values, int i, int accumulator){
    computations ++;

    if(dic[i + 1][accumulator] == NO_ELEMENT) {
        if (i == NO_ELEMENT) {
            if (accumulator == 0)
                dic[i + 1][accumulator] = ZERO;
            else
                dic[i + 1][accumulator] = INFINITY;
        } else {
            if (values[i] > accumulator)
                dic[i + 1][accumulator] = subset_sum(values, i - 1, accumulator);
            else
                dic[i + 1][accumulator] = min(subset_sum(values, i - 1, accumulator),
                                              1 + subset_sum(values, i - 1, accumulator - values[i]));
        }
    }

    return dic[i + 1][accumulator];
}

void dynamic_programming::destroy_dic(int n){
    for (int i = 0; i <= n; i++)
        delete dic[i];

    delete [] dic;
}

void dynamic_programming::print_dic(int n, int t){
    for(int i = 0; i <= n; i++){
        for(int accumulator = 0; accumulator <= t; accumulator++){
            int val = dic[i][accumulator];
            std::cout << val << "    ";
        }

        std::cout << std::endl;
    }
}