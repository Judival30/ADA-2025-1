#include<bits/stdc++.h>
using namespace std;

int SIZE_ARR = 0;
const int  inf = 1e9;


class Node{
    public: 
    int pref,suf,sum,mx;
    Node() {
        pref=suf=mx=-inf;
        sum=0;
    }

    Node operator+(const Node& o) const {
        Node res;
        res.sum = sum+o.sum;
        res.pref = max(pref,sum+o.pref);
        res.suf = max(o.suf,o.sum+suf);
        res.mx = max(max(mx,o.mx),suf+o.pref);
        return res;
    }
};


vector<Node> tree;

void build(const vector<int>& arr, int L = 0, int R = -1, int index = 0){
    if(R == -1) R = SIZE_ARR = arr.size() - 1;

    if(L >= R){
        tree[index] = Node();
        tree[index].pref=tree[index].suf=tree[index].sum=tree[index].mx=arr[L];
    }else{
        int md = L + ((R - L) >> 1);
        int left = index + 1;
        int right = index + (md - L + 1) * 2;
        build(arr, L, md, left);
        build(arr, md + 1, R, right);
        tree[index] = tree[left] + tree[right];
    }
}

void update(int x, int k, int L = 0, int R = SIZE_ARR, int index=0){
    if ( L >= R ) {
        tree[index].pref=tree[index].suf=tree[index].sum=tree[index].mx=arr[L];
    } else if( !( R < l|| L > r) ){
        int md = L + ((R - L) >> 1);
        int left = index + 1;
        int right = index + (md - L + 1) * 2;
        if ( x <= md ) update(x,k,L,md,left);
        else update(x,k,md+1,R,right);
        tree[index] = tree[left] + tree[right];
    }
}

Node query(int l, int r, int k, int L = 0, int R = SIZE_ARR, int index=0){
    Node ans;
    if( l <= L && R <= r) {
        ans = tree[index];
    }else if( !( R < l|| L > r) ){
        int md = L + ((R - L) >> 1);
        int left = index + 1;
        int right = index + (md - L + 1) * 2;
        ans = query(l,r,k,L,md,left) + query(l,r,k,md+1,R,right);
    }
    
    return ans;
}

const int limit = 1e6;
string op[limit];
int x[limit],y[limit];

int bit[limit],b_size;
void build( const vector<int> &arr ){
    b_size = arr.size();
    for ( int i = 1 ; i <= b_size ; ++i ) {
        bit[i] += arr[i-1];
        int ot = i+i&(-i);
        if ( ot <= b_size ) bit[ot] += bit[i];
    }
}
int query( int x ){
    int res = 0;
    for ( ; x <= b_size ; x += x&(-x) ) res += bit[x];
    return res;
}
void update( int x, int vl ){
    for ( ; x ; x-=x&(-x) ) bit[x] += vl;
}

int main(){
    cin.tie(NULL);

    int n; cin >> n;
    vector<int> A(n);
    for(int i = 0; i < n; ++i)cin >> A[i];
    
    
    int q; cin >> q;
    for(int i = 0; i < q; ++i){
        cin >> op[i] >> x[i];
        if ( op[i] != "D" ) cin >> y[i];
        else y[i] = 0;
    }
    
    int tn=n;
    for ( int i = 0 ; i < q ; ++i ) if ( op[i]=="I" ) ++tn;
    tree.resize(tn*2);



    build(a2);

    for ( int i = 0 ; i < q ; ++i ){
        if ( op[i] != "Q" ) update( tx,y[i] );
        else {
            int ty = y[i] + query( y[i] );
            cout << query(tx,ty);
        }
    }

    build(A);
    return 0;
}