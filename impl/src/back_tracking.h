//
// Created by Facundo Linlaud on 8/9/18.
//

#ifndef IMPL_BACK_TRACKING_H
#define IMPL_BACK_TRACKING_H


class back_tracking {
    const int INFINITY = 999;

private:
    int* values;
    int n;

    int bt(int i, int t);

public:
    int computations;

    back_tracking(int values[], int _n);

    int calculate(int t);
};


#endif //IMPL_BACK_TRACKING_H
