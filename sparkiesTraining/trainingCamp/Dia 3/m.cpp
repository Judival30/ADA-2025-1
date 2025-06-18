#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    while (cin >> n){
        vector<int> lst(n);
        for (int i = 0; i < n; i++)
            cin >> lst[i];
        sort(lst.rbegin(), lst.rend());
        for (int h = 0; h < n; h++){
            if (h + 1 <= lst[h])
                ans = h + 1;
            else 
                break;
        }
        cout << ans << endl;
    }
    return 0;
}