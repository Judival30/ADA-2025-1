#include<bits/stdc++.h>
using namespace std;

class State{
public:
    int l,r;
    State()=default;
    State(int l, int r ) : l(l),r(r){};
    State operator +( const State &o ) const {
        return State( max(0,l-o.r)+o.l, max(0,o.r-l)+r );
    }
    bool correct(){return l==r && l == 0;}
    void flip(){
        assert(l+r==1);
        l^=1; r^=1;
    }
};

const int limit = 1e6;
State t[limit];
int t_size;
void build( const vector<State> &arr, int ind=0, int l=0,int r=-1 ){
    if ( r==-1 ) r=t_size=arr.size()-1;

    if ( l>=r ) t[ind]=arr[l];
    else {
        int m=(r+l)/2;
        int rind=ind+2*(m-l+1);
        build(arr, ind+1, l, m);
        build(arr,rind,m+1,r);
        t[ind] = t[ind+1] + t[rind];
    }
}
void update( int x, int ind = 0, int l=0, int r=t_size ) {
    if ( l>=r ) t[ind].flip();
    else {
        int m=(r+l)/2;
        int rind=ind+2*(m-l+1);
        if ( x <= m ) update(x,ind+1,l,m);
        else update(x,rind,m+1,r);
        t[ind]=t[ind+1]+t[rind];
    }
}
bool query(){ return t[0].correct(); }

void solve(){
    int n; cin >> n;
    string cad; cin >> cad;
    vector<State> arr(n);
    for ( int i = 0 ; i < n ; ++i ) {
        int l = arr[i]=='(',r=arr[i]==')';
        arr[i] = State( l,r );
    }
    build(arr);
    int q; cin >> q;
    for ( int i = 0 ; i < q ; ++i ) {
        int x; cin >> x;
        if ( x ) update(x-1);
        else {
            if ( query() ) cout << "YES\n";
            else cout << "NO\n";
        }
    }
}

int main(){
    for ( int t = 1 ; t <= 10 ; ++t ) {
        cout << "Test " << t << ":\n";
        solve();
    }
    return 0;
}