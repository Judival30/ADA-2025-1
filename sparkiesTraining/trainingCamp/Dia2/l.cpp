#include<bits/stdc++.h>
using namespace std;


void solve(){
    int n; cin >> n;
    int x=0;
    for ( int i =0  ; i < n ;++i){
        int act; cin >> act;
        x ^= act;
    }
    cout << x<< " _ _ _ " << endl;
    if ( x ) cout << "Alice\n";
    else cout << "Bob\n";
}
int main(){
    int t; cin >> t;
    while ( t-- ) {
        solve();
    }
    return 0;
}