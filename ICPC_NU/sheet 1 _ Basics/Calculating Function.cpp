# include <iostream>
#include <cmath>
using namespace std;

int main(){
    long long int n;
    cin >> n;
    long long int f;
    // another solution using formula
    // f = pow(-1,n)* (n+1)/2;

    // soulution using if , else
    if (n % 2 == 0){
        f = n/2;
    }
    else{
        f = -(n+1)/2;
    }
    cout<<f<<endl;
    return 0;
}



// solution using loops
/*int main(){
    long long int n;
    cin >> n;
    long long int f = 0;
    
    for (int i = 0; i <=n; i++){
        if (i % 2 == 0 && i <= n){
            f += i;
        }
    else if (i % 2 !=0 && i <= n) {
            f -= i;
        }
    }
    cout << f << endl;

    return 0;

}*/