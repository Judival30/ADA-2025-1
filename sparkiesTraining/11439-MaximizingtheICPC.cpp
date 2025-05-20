#include <bits/stdc++.h>
using namespace std;

// ------------ Código de Blossom (sin cambios) -------------
struct blossom {
    int n, m;
    vector<int> mate;
    vector<vector<int>> b;
    vector<int> p, d, bl;
    vector<vector<int>> g;
    blossom(int n) : n(n) {
        m = n + n/2;
        mate.assign(n, -1);
        b.resize(m);
        p.resize(m);
        d.resize(m);
        bl.resize(m);
        g.assign(m, vector<int>(m, -1));
    }
    void add_edge(int u, int v) {
        g[u][v] = u;
        g[v][u] = v;
    }
    void match(int u, int v) {
        g[u][v] = g[v][u] = -1;
        mate[u] = v;
        mate[v] = u;
    }
    vector<int> trace(int x) {
        vector<int> vx;
        while(true) {
            while(bl[x] != x) x = bl[x];
            if(!vx.empty() && vx.back() == x) break;
            vx.push_back(x);
            x = p[x];
        }
        return vx;
    }
    void contract(int c, int x, int y,
                  vector<int> &vx, vector<int> &vy) {
        b[c].clear();
        int r = vx.back();
        while(!vx.empty() && !vy.empty() && vx.back() == vy.back()) {
            r = vx.back();
            vx.pop_back();
            vy.pop_back();
        }
        b[c].push_back(r);
        b[c].insert(b[c].end(), vx.rbegin(), vx.rend());
        b[c].insert(b[c].end(), vy.begin(), vy.end());
        for(int i = 0; i <= c; i++) {
            g[c][i] = g[i][c] = -1;
        }
        for(int z : b[c]) {
            bl[z] = c;
            for(int i = 0; i < c; i++) {
                if(g[z][i] != -1) {
                    g[c][i] = z;
                    g[i][c] = g[i][z];
                }
            }
        }
                  }
                  vector<int> lift(vector<int> &vx) {
                      vector<int> A;
                      while(vx.size() >= 2) {
                          int z = vx.back(); vx.pop_back();
                          if(z < n) {
                              A.push_back(z);
                              continue;
                          }
                          int w = vx.back();
                          int i = (A.size()%2==0
                          ? find(b[z].begin(), b[z].end(), g[z][w]) - b[z].begin()
                          : 0);
                          int j = (A.size()%2==1
                          ? find(b[z].begin(), b[z].end(), g[z][A.back()]) - b[z].begin()
                          : 0);
                          int k = b[z].size();
                          int dif = ((A.size()%2==0? i%2==1 : j%2==0) ? 1 : k-1);
                          while(i != j) {
                              vx.push_back(b[z][i]);
                              i = (i + dif) % k;
                          }
                          vx.push_back(b[z][i]);
                      }
                      return A;
                  }
                  // Devuelve #aristas en el matching
                  int solve() {
                      for(int ans = 0; ; ans++) {
                          fill(d.begin(), d.end(), 0);
                          queue<int> Q;
                          for(int i = 0; i < m; i++) bl[i] = i;
                          for(int i = 0; i < n; i++) {
                              if(mate[i] == -1) {
                                  Q.push(i);
                                  p[i] = i;
                                  d[i] = 1;
                              }
                          }
                          int c = n;
                          bool aug = false;
                          while(!Q.empty() && !aug) {
                              int x = Q.front(); Q.pop();
                              if(bl[x] != x) continue;
                              for(int y = 0; y < c; y++) {
                                  if(bl[y]==y && g[x][y]!=-1) {
                                      if(d[y]==0) {
                                          p[y]=x; d[y]=2;
                                          p[mate[y]] = y; d[mate[y]] = 1;
                                          Q.push(mate[y]);
                                      } else if(d[y]==1) {
                                          auto vx = trace(x), vy = trace(y);
                                          if(vx.back()==vy.back()) {
                                              contract(c, x, y, vx, vy);
                                              Q.push(c);
                                              p[c]=p[b[c][0]];
                                              d[c]=1;
                                              c++;
                                          } else {
                                              aug = true;
                                              vx.insert(vx.begin(), y);
                                              vy.insert(vy.begin(), x);
                                              auto A = lift(vx);
                                              auto B = lift(vy);
                                              A.insert(A.end(), B.rbegin(), B.rend());
                                              for(int i = 0; i < (int)A.size(); i+=2) {
                                                  match(A[i], A[i+1]);
                                                  if(i+2 < (int)A.size())
                                                      add_edge(A[i+1], A[i+2]);
                                              }
                                          }
                                          break;
                                      }
                                  }
                              }
                          }
                          if(!aug) return ans;
                      }
                  }
};

// ------------- Función para un test con umbral W -------------
bool puedoEmparejar(int N, const vector<tuple<int,int,int>>& edges, int W) {
    int V = 1<<N;
    blossom B(V);
    for(auto &e : edges) {
        int u,v,w; tie(u,v,w) = e;
        if(w >= W)
            B.add_edge(u, v);
    }
    int pares = B.solve();
    return pares * 2 == V;  // matching perfecto
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    for(int tc = 1; tc <= T; tc++){
        int N; cin >> N;
        int W = 1<<N;
        vector<tuple<int,int,int>> edges;
        // Leer matriz triangular de pesos
        for(int i = 0; i < W-1; i++){
            for(int j = i+1; j < W; j++){
                int w; cin >> w;
                edges.emplace_back(i, j, w);
            }
        }
        // Extraer y ordenar pesos únicos
        vector<int> pesos;
        pesos.reserve(edges.size());
        for(auto &e: edges) pesos.push_back(get<2>(e));
        sort(pesos.begin(), pesos.end());
        pesos.erase(unique(pesos.begin(), pesos.end()), pesos.end());

        // Bin‑search sobre índices de 'pesos'
        int lo = 0, hi = (int)pesos.size()-1, ans = pesos[0];
        while(lo <= hi){
            int mid = (lo + hi) / 2;
            if(puedoEmparejar(N, edges, pesos[mid])){
                ans = pesos[mid];
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        cout << "Case " << tc << ": " << ans << "\n";
    }
    return 0;
}
