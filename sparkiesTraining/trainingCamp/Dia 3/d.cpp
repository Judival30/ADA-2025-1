#include<bits/stdc++.h>
using namespace std;

int SIZE_ARR = 0;



class Node{
    public: 
        vector<int> arr;

    Node(const vector<int>& arr): arr(arr) {}
    Node() {}

    Node operator+(const Node& o) const {
        vector<int> ans(arr.size()+o.size());
        int n = arr.size();
        int m = o.arr.size();
        int i = 0, j = 0, k=0;
        while( i < n && j < m){
            if(arr[i] < o.arr[j]){
                ans[k++] = (arr[i++]);
            }else{
                ans[k++] = (o.arr[j++]);
            }
        }
        while(i < n){
            ans[k++] = (arr[i++]);
        }
        while(j < m){
            ans[k++] = (o.arr[j++]);
        }
        return Node(ans);
    }
};


vector<Node> tree;

void build(const vector<int>& arr, int L = 0, int R = -1, int index = 0){
    if(R == -1) R = SIZE_ARR = arr.size() - 1;

    if(L >= R){
        tree[index] = Node({arr[L]});
    }else{
        int md = L + ((R - L) >> 1);
        int left = index + 1;
        int right = index + (md - L + 1) * 2;
        build(arr, L, md, left);
        build(arr, md + 1, R, right);
        tree[index] = tree[left] + tree[right];
    }
}

int binarySearch(const vector<int>& arr, int k){
    int l = 0, r = arr.size() - 1;
    int ans = arr.size();
    while (l <= r){
        int md = l + ((r - l) >> 1);
        if(arr[md] <= k){
            l = md + 1;
        }else{
            r = md - 1;
            ans = min(ans, md);
        }
    }
    return arr.size() - ans;
}

int query(int l, int r, int k, int L = 0, int R = SIZE_ARR, int index=0){
    int ans = 0;
    if( l <= L && R <= r) {
        ans = binarySearch(tree[index].arr, k);
        //cout <<L << " _ " << R << " -> " << ans << endl;
        //cout << l<< " ? " << r << endl;
    }else if( !( R < l|| L > r) ){
        int md = L + ((R - L) >> 1);
        int left = index + 1;
        int right = index + (md - L + 1) * 2;
        ans = query(l,r,k,L,md,left) + query(l,r,k,md+1,R,right);
    }
    
    return ans;
}

int main(){
    cin.tie(NULL);

    int n; cin >> n;
    vector<int> A(n);
    tree.resize(n*2);
    for(int i = 0; i < n; ++i)cin >> A[i];
    build(A);
    int q; cin >> q;
    for(int i = 0; i < q; ++i){
        int l, r, k; cin >> l >> r >> k;
        cout << query(l - 1, r - 1, k) << '\n';
    }
    return 0;
}