# include <iostream>
# include <string>
using namespace std;

int main(){
    int t;
    cin>>t;
    string door;
    string baseString = "abc";
    char arr[3] = {'a', 'b', 'c'};
    string arr2[t];

    for(int i = 0; i < t; i++){
        cin >> door;
        int counter = 0; 
        for(int j = 0; j < 3 ;j++){
            if(door[j] == arr[j]){
                counter++;
            }
        }
        if(counter >= 1){
            arr2[i] = "YES";
        }
        else{
            arr2[i] = "NO";
        }
    }
    for(string res : arr2){cout<<res<<endl;}

    return 0;
}