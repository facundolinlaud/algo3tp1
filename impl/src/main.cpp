#include <iostream>
#include <string>
#include "dynamic_programming.h"

using namespace std;

static const int ZERO = 0;
static const int NO_ELEMENT = -1;
static const int INFINITY = 999;

int** dic;

int min(int a, int b){
    if(a < b) return a;
    return b;
}

void initialize_dic(int n, int t){
    dic = new int*[n + 1];

    for(int i = 0; i <= n; i++){
        dic[i] = new int[t + 1];

        for(int accumulator = 0; accumulator <= t; accumulator++){
            dic[i][accumulator] = -1;
        }
    }
}

//void print(){
//    for(int i = 0; i <= n; i++){
//        for(int accumulator = 0; accumulator <= T; accumulator++){
//            int val = dic[i][accumulator];
//            cout << val << "    ";
//        }
//
//        cout << endl;
//    }
//}

int subset_sum(int* values, int i, int accumulator){
    if(dic[i + 1][accumulator] == NO_ELEMENT) {
        if (i == NO_ELEMENT)
            if (accumulator == 0)
                dic[i + 1][accumulator] = ZERO;
            else
                dic[i + 1][accumulator] = INFINITY;
        else
            if (values[i] > accumulator)
                dic[i + 1][accumulator] = subset_sum(values, i - 1, accumulator);
            else
                dic[i + 1][accumulator] = min(subset_sum(values, i - 1, accumulator),
                                              1 + subset_sum(values, i - 1, accumulator - values[i]));
    }

    return dic[i + 1][accumulator];
}

void destroy_dic(int n){
    for (int i = 0; i <= n; i++)
        delete dic[i];

    delete [] dic;
}

int main(int argc, char *argv[]) {
    if(argc < 2){
        cout << "./ejec {T} {n} {v1} ... {vn}" << endl;
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

    int resultado;
    if(arguments[1] == "pd") {
        dynamic_programming dp;
        resultado = dp.calculate(n, t, values);
    }

    cout << "##################" << endl;
    cout << "Resultado: " << resultado << endl;
    cout << "##################" << endl;

    return 0;
}