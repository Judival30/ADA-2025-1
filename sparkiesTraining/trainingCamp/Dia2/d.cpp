#include<bits/stdc++.h>
using namespace std;

typedef long long lint;

int main(){
    string s; cin >> s;
    while( s != "*"){
        lint n = s.size();
        lint res=1;
        for(lint i = 0; i < n; ++i){
            if( s[i] == 'Y'){
                res = (res*(i+1ll))/__gcd(res,i+1ll);
            }
        }
        bool flag = true;
        for(lint i = 0; i < n; ++i){
            if(s[i] == 'N' && ((res%(i +1ll)) == 0ll)){
                flag = false;
            }
        }
        if (flag){
            cout << res;
        }else{
            cout << -1;
        }
        cout << endl;
        cin >> s;
    }
    return 0;
}