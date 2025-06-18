#include<bits/stdc++.h>
using namespace std;

class Query{
public:
    int ind, l, r;
    Query()=default;
    bool operator < ( const Query &qq ) const { return r < qq.r ; }
};

const int  inf = 1e9, limit=1e6;
int a[limit], all[limit];
Query qu[limit];
int res[limit];

int main(){
    int n; cin >> n;
    
    for ( int i = 0 ; i < n ; ++i ) cin >> a[i];
    {
        vector<int> tmp(n);
        for ( int i = 0 ; i < n ; ++i ) tmp[i] = a[i];
        sort(tmp.begin(),tmp.end());
        map<int,int> ren;
        int cnt = 0; ren[tmp[0]] = 0;
        for ( int i= 1 ; i < n ; ++i ){
          //cout << i << " _ " << tmp[i] << " ? " << tmp[i-1] << endl;
            if ( tmp[i] != tmp[i-1] ) ren[tmp[i]]=++cnt;
        }
        for ( int i = 0 ; i < n ; ++i ) a[i] = ren[a[i]];
    }
    //cout << "[a]"; for ( int i = 0 ; i < n ; ++i ) cout << ' ' << a[i]; cout << endl;


    int q; cin >> q;
    for ( int i = 0 ; i < q ; ++i ) cin >> qu[i].l >> qu[i].r;
    for ( int i = 0 ; i < q ; ++i ) {
        qu[i].ind = i;
        --qu[i].l; --qu[i].r;
    }
    memset(all,0,sizeof(int)*n);
    int sq=1;
    while ( sq*sq < n ) ++sq;
    vector<vector<Query>> box(sq+1);
    for ( int i = 0 ; i < q ; ++i ) box[qu[i].l/sq].push_back(qu[i]);
    for ( int i = 0 ; i <= sq ; ++i ) sort(box[i].begin(),box[i].end());
    //cout << " ? ? ? ? " << endl;
    int l = 0,r=0, cnt=1; all[a[0]]=1;
    for ( int i = 0 ; i <= sq ; ++i ){
        for ( const Query &act : box[i] ){
            while ( r > act.r ) {
                --all[a[r]];
                if ( all[a[r]] == 0 ) --cnt;
                --r;
            }
            while ( r < act.r ){
                ++r;
                if ( all[a[r]] == 0 ) ++cnt;
                ++all[a[r]];
            }
            //cout << cnt << " ? ? ? " << r << " * " << l << endl;
            while ( l < act.l ) {
                --all[a[l]];
                if ( all[a[l]] == 0 ) --cnt;
                ++l;
            }
            //cout << cnt << " ? ? ? " << r << " * " << l << endl;
            while ( l > act.l ) {
                --l;
                if ( all[a[l]] == 0 ) ++cnt;
                ++all[a[l]];
            }
            
            //cout << l<< " _ _ " << r <<  " _ " << act.ind << " -> " << cnt << endl;
            res[act.ind] = cnt;
        }
    }

    for ( int i = 0 ; i < q ; ++i ) cout << res[i] << '\n';
    return 0;
}