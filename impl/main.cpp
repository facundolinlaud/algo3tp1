#include <iostream>
using namespace std;

static const int ZERO = 0;
static const int NO_ELEMENT = -1;
static const int INFINITY = 999;

const int n = 5;
const int T = 25;

int V[n] = {10, 15, 5, 10, 5};
int dic[n + 1][T + 1];

int min(int a, int b){
    if(a < b) return a;
    return b;
}

void initialize_dic(){
    for(int i = 0; i <= n; i++){
        for(int accumulator = 0; accumulator <= T; accumulator++){
            dic[i][accumulator] = -1;
        }
    }
}

void print(){
    for(int i = 0; i <= n; i++){
        for(int accumulator = 0; accumulator <= T; accumulator++){
            int val = dic[i][accumulator];
            cout << val << "    ";
        }

        cout << endl;
    }
}

int f(int i, int accumulator){
    if(dic[i + 1][accumulator] == NO_ELEMENT) {
        if (i == NO_ELEMENT)
            if (accumulator == 0)
                dic[i + 1][accumulator] = ZERO;
            else
                dic[i + 1][accumulator] = INFINITY;
        else
            if (V[i] > T)
                dic[i + 1][accumulator] = f(i - 1, accumulator);
            else
                dic[i + 1][accumulator] = min(f(i - 1, accumulator), 1 + f(i - 1, accumulator - V[i]));
    }

    return dic[i + 1][accumulator];
}

int main() {
    initialize_dic();
    int min_cardinal = f(n - 1, T);

    print();
    cout << "== Answer: ==" << endl;
    cout << min_cardinal << endl;
}