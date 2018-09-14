#include <iostream>
#include "dynamic_programming.h"
#include "brute_force.h"
#include "back_tracking.h"
#include <limits>
#include <time.h>
#include <iomanip>

using namespace std;

typedef std::numeric_limits< double > dbl;

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

    clock_t start, end;
    start = clock();

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

    end = clock();
//    cout.precision(dbl::max_digits10);
    double cpu_ticks_used = (double) (end - start);
    double cpu_time_used = cpu_ticks_used / CLOCKS_PER_SEC;

    cout << "##################" << endl;
    cout << "Algoritmo: " << arguments[1] << endl;
    cout << "Resultado: " << result << endl;
    cout << "Recursiones: " << computations << endl;
    cout << "Ticks: " << cpu_ticks_used << endl;
    cout << "Segundos: " << fixed << std::setprecision(15) << cpu_time_used << endl;
    cout << "##################" << endl;

    return 0;
}