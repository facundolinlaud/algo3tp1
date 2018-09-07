//
// Created by Facundo Linlaud on 5/9/18.
//

#ifndef IMPL_DYNAMIC_PROGRAMMING_H
#define IMPL_DYNAMIC_PROGRAMMING_H

class dynamic_programming {
    const int ZERO = 0;
    const int NO_ELEMENT = -1;
    const int INFINITY = 999;

private:
    int** dic;

    void destroy_dic(int n);

    int subset_sum(int* values, int i, int accumulator);

    void initialize_dic(int n, int t);

public:
    int computations;

    dynamic_programming();

    int calculate(int n, int t, int values[n]);

    void print_dic(int n, int t);
};
#endif //IMPL_DYNAMIC_PROGRAMMING_H
