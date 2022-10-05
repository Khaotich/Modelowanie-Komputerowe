#include <iostream>
#include <fstream>
#include <random>
#include <time.h>

using namespace std;

auto rand_cpp()
{
    return rand()/float(RAND_MAX + 1);
}

mt19937 mt(time(NULL));
uniform_real_distribution<double> random(0, 1.0);
auto my_random()
{
    return random(mt);
}

int main()
{
    srand(time(NULL));

    const long int N = 10000;
    const long long int P = 1000000;

    ofstream my_r("my_random");
    ofstream cpp_rand("rand");

    long int tab_cpp[N] = {0};
    long int tab_my[N] = {0};

    for(int i=0; i < P; ++i)
    {
        auto x_my = my_random();
        auto x_cpp = rand_cpp();
        int r_my = int(floor(x_my * N));
        int r_cpp = int(floor(x_cpp * N));
        tab_my[r_my]++;
        tab_cpp[r_cpp]++;
    }

    for(int i=0; i < N; ++i)
    {
        my_r << i << " " << tab_my[i] << endl;
        cpp_rand << i << " " << tab_cpp[i] << endl;
    }
}
