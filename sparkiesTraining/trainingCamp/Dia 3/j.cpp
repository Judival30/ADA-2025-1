#include <bits/stdc++.h>

using namespace std;
const int inf = 1e9;

class Edge{
public:
    int u,v,w,cnt;
    Edge()=default;
    Edge(int u,int v,int w):u(u),v(v),w(w),cnt(0){};
};

vector<vector<Edge>> G;

vector<int> dijkstra(int s){
    int n = G.size();
    vector<int> dist(n, 1e9);
    priority_queue<pair<int,int>> q; q.push({0,s}); dist[s]=0;
    while( !q.empty() ){
        int u = q.top().second, du = q.top().first; q.pop();
        cout << u << "_ _ _ _ _ _ _ _ " << endl;
        if( -du == dist[u]){
            //cout << "entra xd " << endl;
            for( const Edge &e : G[u] ){
                int v = e.v, duv = e.w;
                //cout << " ? ? ? ? " << v << endl;
                if( -du + duv < dist[v]){
                    dist[v] = -du + duv;
                    q.push({du-duv,v});
                }
            }
        }
    }
    return dist;
}
int long_dist( const vector<vector<pair<int,int>>> &dag, int nd, vector<int> &mem  ){
    int res=0;
    if ( mem[nd] >= 0 ) res = mem[nd];
    else {
        for ( const pair<int,int> &e : dag[nd] ){
            res = max(res,long_dist(dag,e.first,mem)+e.second);
        }
        mem[nd] = res;
    }
    return res;
}


int main(){
    int J, B, C, N, S; cin >> J >> B >> C >> N >> S;
    while(J != -1){
        int n = J;
        G = vector<vector<Edge>>(J);
        for(int i = 0; i < S; ++i){
            int u, v, dist;  cin >> u >> v >> dist;
            --u; --v;
            G[u].push_back({u,v, dist});
            G[v].push_back({v,u, dist});
            cout << u << " _ _ _ _ _ " << v << endl;
        }
        vector<int> dist = dijkstra(B-1);
        for ( int obj : {C-1,N-1} ){
            vector<bool> vis(n,0);
            stack<int> s; s.push(obj);
            while ( !s.empty() ){
                int act = s.top();s.pop();
                for ( Edge &e : G[act] ) {
                    int df_cost = dist[e.v]-dist[e.u];
                    if ( df_cost == e.w ) {
                        ++e.cnt;
                        if ( !vis[e.u] ) {
                            vis[e.u]=1; s.push(e.u);
                        }
                    }
                }
            }
        }

        vector<vector<pair<int,int>>> dag( n );
        for ( int i = 0 ; i < n ; ++i ) {
            for ( const Edge &e : G[i] ){
                if ( e.cnt == 2 ) {
                    dag[e.u].push_back({e.v,e.w});
                    cout << "agrego " << e.u << " _ " << e.v << endl;
                }
            }
        }
        vector<int> mem(n,-1);
        int res = long_dist( dag, B-1, mem );
        cout << res << ' ' << dist[C-1]-res << ' ' << dist[N-1]-res << '\n';
        
        cin >> J >> B >> C >> N >> S;
    }
    return 0;
}