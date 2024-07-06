# include <iostream>
using namespace std;
#include <cmath>

int main (){
    long long int n, m, a;
    cin >> n >> m >> a;
    long long int flagstonesNumber;
    flagstonesNumber = ceil(static_cast<double>(n) / a) * ceil(static_cast<double>(m) / a);
    cout<< flagstonesNumber;
    return 0;
}