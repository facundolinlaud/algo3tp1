#include <iostream>
#include <string>
#include "dynamic_programming.h"

using namespace std;

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