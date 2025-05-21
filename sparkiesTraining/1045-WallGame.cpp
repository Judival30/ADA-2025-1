/*
Autor: Juan Diego Valencia Alomia
uva: 1045 The Great Wall Game
Fuente de Hungarian:
https://www.geeksforgeeks.org/hungarian-algorithm-assignment-problem-set-1-introduction/
https://www.topcoder.com/thrive/articles/Assignment%2520Problem%2520and%2520Hungarian%2520Algorithm
*/

#include <bits/stdc++.h>
using namespace std;

class Hungarian
{
private:
    vector<vector<int>> cost_matrix;
    int n;
    vector<int> u, v, p, way;

public:
    Hungarian(const vector<vector<int>> &matrix) : cost_matrix(matrix)
    {
        n = matrix.size();
        u.resize(n + 1, 0);
        v.resize(n + 1, 0);
        p.resize(n + 1, 0);
        way.resize(n + 1, 0);
    }

    int compute()
    {
        for (int i = 1; i <= n; ++i)
        {
            p[0] = i;
            vector<int> minv(n + 1, INT_MAX);
            vector<bool> used(n + 1, false);
            int j0 = 0;
            bool flag = true;
            while (flag)
            {
                used[j0] = true;
                int i0 = p[j0];
                int delta = INT_MAX;
                int j1 = 0;
                for (int j = 1; j <= n; ++j)
                {
                    if (!used[j])
                    {
                        int cur = cost_matrix[i0 - 1][j - 1] - u[i0] - v[j];
                        if (cur < minv[j])
                        {
                            minv[j] = cur;
                            way[j] = j0;
                        }
                        if (minv[j] < delta)
                        {
                            delta = minv[j];
                            j1 = j;
                        }
                    }
                }
                for (int j = 0; j <= n; ++j)
                {
                    if (used[j])
                    {
                        u[p[j]] += delta;
                        v[j] -= delta;
                    }
                    else
                    {
                        minv[j] -= delta;
                    }
                }
                j0 = j1;
                if (p[j0] == 0)
                    flag = false;
            }
            flag = true;
            while (flag)
            {
                int j1 = way[j0];
                p[j0] = p[j1];
                j0 = j1;
                if (j0 == 0)
                    flag = false;
            }
        }
        int total_cost = 0;
        for (int j = 1; j <= n; ++j)
        {
            total_cost += cost_matrix[p[j] - 1][j - 1];
        }
        return total_cost;
    }
};

int solve(int n, vector<vector<pair<int, int>>> &lines, vector<pair<int, int>> &pos)
{
    int ans, si, sj, di, dj;
    ans = INT_MAX;
    for (vector<pair<int, int>> &line : lines)
    {
        vector<vector<int>> matCost(n, vector<int>(n));
        for (int i = 0; i < n; ++i)
        {
            si = pos[i].first;
            sj = pos[i].second;
            for (int j = 0; j < n; ++j)
            {
                di = line[j].first;
                dj = line[j].second;
                matCost[i][j] = abs(si - di) + abs(sj - dj);
            }
        }
        Hungarian h(matCost);
        int cost = h.compute();
        ans = min(ans, cost);
    }
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, r, c;
    int t = 0;
    while (cin >> n, n != 0)
    {
        t++;
        vector<pair<int, int>> pos;
        for (int i = 0; i < n; ++i)
        {
            cin >> r >> c;
            pos.push_back({r, c});
        }

        vector<vector<pair<int, int>>> lines;

        // Rows, cols, diags
        vector<pair<int, int>> diag1, diag2;
        for (int i = 1; i <= n; ++i)
        {
            vector<pair<int, int>> row, col;
            for (int j = 1; j <= n; ++j)
            {
                row.push_back({i, j});
                col.push_back({j, i});
            }
            lines.push_back(row);
            lines.push_back(col);
            diag1.push_back({i, i});
            diag2.push_back({i, n + 1 - i});
        }
        lines.push_back(diag1);
        lines.push_back(diag2);

        cout << "Board " << t << ": " << solve(n, lines, pos) << " moves required.\n\n";
    }
    return 0;
}