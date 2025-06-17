#include<bits/stdc++.h>
using namespace std;

typedef long long lint;

lint magic( lint x ){
    lint res;
    if ( x) {
        res = (x&1)?0:x;
        res ^= (((x-1ll)>>1)&1)^1;
    } else res = 0;
    return  res;

}

int main(){
    int n; cin >> n;
    lint res = 0;
    for ( int i = 0 ; i < n ; ++ i){
        lint x,m; cin >> x >> m;
        res ^= magic(x-1)^magic(x+m-1);
    }
    if ( res ) cout << "tolik\n";
    else cout << "bolik\n";
    return 0;
}