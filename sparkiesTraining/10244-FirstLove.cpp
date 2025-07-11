// C++ implementation of
// the above approach
#include <bits/stdc++.h>
using namespace std;

unordered_set<string> seen;
vector<int> edges;

// Modified DFS in which no edge
// is traversed twice
void dfs(string node, int& k, string& A)
{
    for (int i = 0; i < k; ++i) {
        string str = node + A[i];
        if (seen.find(str) == seen.end()) {
            seen.insert(str);
            dfs(str.substr(1), k, A);
            edges.push_back(i);
        }
    }
}

// Function to find a de Bruijn sequence
// of order n on k characters
string deBruijn(int n, int k, string A)
{

    // Clearing global variables
    seen.clear();
    edges.clear();

    string startingNode = string(n - 1, A[0]);
    dfs(startingNode, k, A);

    string S;

    // Number of edges
    int l = pow(k, n);
    for (int i = 0; i < l; ++i)
        S += A[edges[i]];
    S += startingNode;

    return S;
}

// Driver code
int main()
{
    int n, k;
    string A ;
    while (cin >> A >> n){
        k = A.size();
        long long s = pow(k, n) + n - 1 ;
    
        if (10000 > s){
            cout << s << endl
                << deBruijn(n, k, A) << endl;
        }
        else{
            cout << s << endl
                << "TOO LONG TO PRINT." << endl;
        }
    
    }
    return 0;
}