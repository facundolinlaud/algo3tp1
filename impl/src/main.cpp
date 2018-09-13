#include <iostream>
#include "dynamic_programming.h"
#include "brute_force.h"
#include "back_tracking.h"

using namespace std;

int main(int argc, char *argv[]) {
    if(argc < 3){
        cout << "./ejec {bf/bt/pd} {T} {n} {v1} ... {vn}" << endl;
        return 0;
    }

    string arguments[argc];

    for(int i = 0; i < argc; i++){
        arguments[i] = string(argv[i]);
    }

    int t = stoi(arguments[2]);
    int n = stoi(arguments[3]);
    int values[n];

    for(int i = 0; i < n; i++){
        values[i] = stoi(arguments[i + 4]);
    }

    int result;
    int computations;

    if(arguments[1] == "bf") {
        brute_force bf(values, n);
        result = bf.calculate(t);
        computations = bf.computations;
    }else if(arguments[1] == "bt") {
        back_tracking bt(values, n);
        result = bt.calculate(t);
        computations = bt.computations;
    }else if(arguments[1] == "dp") {
        dynamic_programming dp;
        result = dp.calculate(n, t, values);
        computations = dp.computations;
    }else{
        cout << "Unrecognized algorithm!" << endl;
        return 0;
    }

    cout << "##################" << endl;
    cout << "Resultado: (" << arguments[1] << ") " << result << " en " << computations << " computaciones" << endl;
    cout << "##################" << endl;

    return 0;
}