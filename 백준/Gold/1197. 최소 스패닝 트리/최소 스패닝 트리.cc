#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int p[10005];
int find(int v){
    if (v==p[v])
        return v;
    else{
        p[v] = find(p[v]);
        return p[v];
    }
}

void marge(int u, int v){
    if (u==v){
        return;
    }
    u = find(u);
    v = find(v);
    p[u] = v;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int v,e;
    int a,b,c;
    long long r = 0;
    cin >> v >> e;
    vector<vector<int>> x; 
    for (int i=0; i < e; i++){
        cin >> a >> b >> c;
        x.push_back({c,a,b});
    }
    sort(x.begin(),x.end());
    for (int i=0; i<v; i++){
        p[i] = i;
    }
    for (int i=0; i < e; i++){
        c = x[i][0];
        b = x[i][1];
        a = x[i][2];
        if (find(a) != find(b)){
            r += c;
            marge(a,b);
        }
    }
    cout << r;
    return 0;
}