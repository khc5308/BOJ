#include <iostream>
using namespace std;
int arr[7000][7000] = {0};
void set(int i,int j){
    for (int k=0; k<3;k++){
        arr[i][j+k] = 1;
        arr[i+2][j+k] = 1;
    }
    arr[i+1][j] = 1;
    arr[i+1][j+2] = 1;
    
}
void re(int x, int y, int n){
    if (n == 3)
        set(x,y);
    else{
        re(x,y,n/3);
        re(x+n/3,y,n/3);
        re(x+n/3 * 2,y,n/3);
        re(x,y+n/3,n/3);
        re(x+n/3*2,y+n/3,n/3);
        re(x,y+n/3*2,n/3);
        re(x+n/3,y+n/3*2,n/3);
        re(x+n/3*2,y+n/3*2,n/3);

    }
}

int main() {
    int n;
    cin >> n;
    re(0,0,n);
    for (int i=0; i<n;i++){
        for (int j=0; j<n; j++){
            if (arr[i][j])
                cout << "*";
            else
                cout << " ";
        }
        cout << endl;
    }
}