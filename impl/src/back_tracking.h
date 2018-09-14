//
// Created by Facundo Linlaud on 8/9/18.
//

#ifndef IMPL_BACK_TRACKING_H
#define IMPL_BACK_TRACKING_H


class back_tracking {
    const long INFINITY = 999999;
    const int NO_ELEMENT = -1;

private:
    int* values;
    int n;
    long minimum_cardinal_so_far;

    long bt(int i, int t, long cardinal_so_far);

public:
    long computations;

    back_tracking(int values[], int _n);

    long calculate(int t);
};


#endif //IMPL_BACK_TRACKING_H
