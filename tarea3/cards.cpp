#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

typedef pair<int, int> pii;
const int INF = numeric_limits<int>::max();

long long dijkstra(vector<vector<pii>> &g, int n)
{
    vector<int> dist(n, INF);
    priority_queue<pii, vector<pii>, greater<pii>> pq;

    dist[0] = 0;
    pq.push({0, 0});
    pii tmp;
    long long ans = 0;
    while (!pq.empty())
    {
        int curd = pq.top().first;
        int u = pq.top().second;
        pq.pop();
        for (int i = 0; i < g[u].size(); i++)
        {
            tmp = g[u][i];
            int v = tmp.first;
            int w = tmp.second;

            if (curd + w < dist[v])
            {
                if (dist[v] != INF)
                    ans -= dist[v];
                dist[v] = curd + w;
                ans += dist[v];
                pq.push({dist[v], v});
            }
        }
    }

    return ans;
}

long long solve(vector<vector<pii>> &gi, vector<vector<pii>> &gt, int n)
{
    long long dist1 = dijkstra(gi, n);
    long long dist2 = dijkstra(gt, n);

    /* long long ans = 0;
    for (int d : dist1)
        ans += d;
    for (int d : dist2)
        ans += d; */

    return dist1 + dist2;
}

int main()
{

    int t, n, e, u, v, w;
    cin >> t;

    while (t--)
    {

        cin >> n >> e;

        vector<vector<pii>> gi(n), gt(n);

        for (int i = 0; i < e; i++)
        {

            cin >> u >> v >> w;
            u--;
            v--;

            gi[u].push_back({v, w});
            gt[v].push_back({u, w});
        }

        cout << solve(gi, gt, n) << endl;
    }

    return 0;
}
