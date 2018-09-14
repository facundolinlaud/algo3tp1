//
// Created by Facundo Linlaud on 8/9/18.
//

#include <iostream>
#include "back_tracking.h"
#include "utils.h"

back_tracking::back_tracking(int _values[], int _n) : values(_values), n(_n), minimum_cardinal_so_far(INFINITY){}

long back_tracking::bt(int i, int t, long cardinal_so_far) {
    computations ++;

    if(cardinal_so_far >= minimum_cardinal_so_far){
        return INFINITY;
    }

    if(i == NO_ELEMENT){
        if(t == 0){
            if(cardinal_so_far < minimum_cardinal_so_far)
                minimum_cardinal_so_far = cardinal_so_far;

            return 0;
        }else{
            return INFINITY;
        }
    }else if(values[i] > t){
        return bt(i - 1, t, cardinal_so_far);
    }else{
        return min(bt(i - 1, t, cardinal_so_far), 1 + bt(i - 1, t - values[i], cardinal_so_far + 1));
    }
}

long back_tracking::calculate(int t){
    return bt(n - 1, t, 0);
}