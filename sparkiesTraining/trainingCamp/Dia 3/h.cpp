#include<bits/stdc++.h>
using namespace std;

void solve(string &a, string &b){
    int n = a.size();
    vector<bool> eq(n);
    for ( int i = 0; i < n ; ++i ) eq[i]= a[i]==b[i];
    int res = 0; bool prev=0;
    for ( int i = 0 ; i < n ; ++i ){
        if ( eq[i] && !prev ){
            prev=1; ++res;
        } else if ( !eq[i] ) prev=0; 
    }
    cout << res << '\n';
}

int main(){
    string a,b; cin >> a >> b;
    while ( a != "*" ){
        solve(a,b);
        cin >> a >> b;
    }
    return 0;
}