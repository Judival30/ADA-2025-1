#include<bits/stdc++.h>
using namespace std;

void solve(int n, int k){

    vector<int> lst(n);
    for(int i =0; i< n; i++){
        cin >> lst[i];
    }
    bool flag = true;
    int i = 0;
    for (int i = 0; i < n; i++){
        int j = 0;
        while(lst[i] >= k && j < 3){
            lst[i] -= k;
            j++;
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++){
        ans += lst[i];
    }
    cout << ans << endl;


    
}

int main(){
    int a,b; cin >> a >> b;
    solve(a,b);
        
    return 0;
}