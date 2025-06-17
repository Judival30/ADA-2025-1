#include<bits/stdc++.h>
using namespace std;

typedef long long lint;
vector<pair<int, int>> cord = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

vector<string> G;
int n, m;

class State {
    public:
    int x, y, dist;
    bool door;
    
    State(int x, int y, int dist, bool door): x(x), y(y), dist(dist), door(door) {}

    bool escape(){
        return  0 > x ||  x >= n || 0 > y || y >= m;
    }

    State* new_state(pair<int, int>& dir){
        bool new_doors;
        if( G[x][y] == 'C'){
            new_doors = false;
        }else if ( G[x][y] == 'O'){
            new_doors = true;
        }else{
            new_doors = door;
        }

        int xk = x + dir.first, yk = y + dir.second;

        State* w = new State(xk, yk, dist + 1, new_doors);
        if (0 <= xk && xk < n && 0 <= yk && yk < m){
            if (G[xk][yk] == 'W'){
                w =  NULL;
            }else if (G[xk][yk] == 'D' && !new_doors){
                w = NULL;
            }
        }         
        return w; 
    }
    
    bool operator<(const State& other) const {
      bool ans;
      if (x != other.x){
        ans = x < other.x;
      } else if (y != other.y){
        ans = y < other.y;
      } else{
        ans = door < other.door;
      }
      return ans;
    }
};




int bfs(State& s){
    set<State> vis; vis.insert(s);
    queue<State*> q; q.push(&s);
    int ans = -1;
    while (!q.empty() && ans == -1){
        State* u = q.front(); q.pop(); 
        if (u->escape()){
            ans = u->dist;
        }else{
            for(int i = 0; i < 4; ++i){
                State* v = u->new_state(cord[i]);
                if(v != NULL && !vis.count(*v)){
                    vis.insert(*v);
                    q.push(v);
                }
            }
        }
    }
    return ans;
}

int main(){
    cin >> n >> m;
    while (n != -1){
        string line;
        pair<int, int> s;
        G = {};
        for (int i = 0; i < n; i++){
            cin >> line;
            for (int j = 0; j < m; j++){
                if (line[j]  == 'H')
                    s = {i, j};
            }
            G.push_back(line);
        }
        State ss(s.first, s.second, 0, false);
        int ans = bfs(ss);
        cout << ans << endl;
        cin >> n >> m;
    }
    return 0;
}