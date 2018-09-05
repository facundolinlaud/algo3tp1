//
// Created by Facundo Linlaud on 5/9/18.
//

#ifndef IMPL_DYNAMIC_PROGRAMMING_H
#define IMPL_DYNAMIC_PROGRAMMING_H

class dynamic_programming {
private:
    int** dic;

    void destroy_dic(int n);

    int subset_sum(int* values, int i, int accumulator);

    void initialize_dic(int n, int t);

    int min(int a, int b);

public:
    dynamic_programming();

    int calculate(int n, int t, int values[n]);
};
#endif //IMPL_DYNAMIC_PROGRAMMING_H
