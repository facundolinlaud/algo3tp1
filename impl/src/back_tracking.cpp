//
// Created by Facundo Linlaud on 8/9/18.
//

#include "back_tracking.h"
#include "utils.h"

back_tracking::back_tracking(int _values[], int _n) : values(_values), n(_n){}

int back_tracking::bt(int i, int t) {
    computations ++;

    if(i == 0){
        if(t == 0){
            return 0;
        }else{
            return INFINITY;
        }
    }else if(values[i] > t){
        return bt(i - 1, t);
    }else{
        return min(bt(i - 1, t), 1 + bt(i - 1, t - values[i]));
    }
}

int back_tracking::calculate(int t){
    return bt(n, t);
}