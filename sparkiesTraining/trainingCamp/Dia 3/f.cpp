#include<bits/stdc++.h>
using namespace std;

class Data{
    public:
    int pref,suf,sum,mx;
    Data( int x ) : pref(x),suf(x),sum(x),mx(x) {};
    Data() {
        pref=suf=mx=-inf;
        sum=0;
    }
    Data operator+(const Data& o) const {
        Data res;
        res.sum = sum+o.sum;
        res.pref = max(pref,sum+o.pref);
        res.suf = max(o.suf,o.sum+suf);
        res.mx = max(max(mx,o.mx),suf+o.pref);
        return res;
    }
};
class Node{
    public:
    int sz,key; Data dat;
    Node *lf, *rf;
    Node(){ 
        sz=1; lf=rf=NULL;
        key = rand();
    }
    bool child(){
        return lf==NULL && rf==NULL;
    }
};

void split( Node* rt, int k, Node *r, Node* l ){
    if ( rt.child() ) return;
    else if  ( rt->lf >= k ) split(rt->lf,k,l,rt->lf),r=rt;
    else split(rt->lf,k,rt->rf,r),l=rt;
}
void merge( Node *rt, Node*r, Node*l ) 

int main(){
    srand(NULL);

    return 0;
}