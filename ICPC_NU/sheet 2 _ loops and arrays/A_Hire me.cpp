#include <iostream>
// #include <bits/stdc++.h>
using namespace std;
// #define ll long long
int main(){
    int n;
    cin >> n;
    int lista[n]{};

    for (int i = 0; i < n; i++){
        cin >> lista[i];
    }
    

    int untreated = 0;
    int hired = 0;

    for(int i; i < n; i++){
        if (lista[i] == -1){
            untreated++;
        }
        else if(lista[i] != -1){
            hired += lista[i];
            for(int j = 1; j <= lista[i]; j++){
                lista[i+j] = 0;
            }
        }
    }
    cout << untreated;
    // for (int i = 0; i < n; ++i){
    //     cout <<"element " << i+1 << " : " << lista[i] << "\n";
    // }
}