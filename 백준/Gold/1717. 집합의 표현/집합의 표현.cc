#include <iostream>
using namespace std;
int p[1000005];
int sz[1000005];
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
    int n,m;
    int a,b,c;
    cin >> n >> m;
    
    for (int i=0; i<=n; i++){
        p[i] = i;
    }

    
    for (int i=0; i < m; i++){
        cin >> a >> b >> c;
        if (a == 0){
            marge(b,c);
        }
        else{
            if (find(b)==find(c))
                cout << "YES" << "\n";
            else
                cout << "NO" << "\n";
        }
    
    }
    
    return 0;
}