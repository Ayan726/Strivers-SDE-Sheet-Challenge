#include <queue>
#include <vector>
#include <string>

bool bfs(int node, vector<vector<int>>& adj, vector<int> &vis) {
    queue<pair<int,int>> q;
    q.push({node, -1});
    vis[node] = 1;

    while (!q.empty()) {
        int f = q.front().first;
        int parent = q.front().second;
        q.pop();

        for (auto it : adj[f]) {
            if (!vis[it]) {
                vis[it] = 1;
                q.push({it, f});
            } else if (vis[it] && it != parent) {
                return true;
            }
        }
    }

    return false;
}

string cycleDetection(vector<vector<int>>& edges, int n, int m) {
    vector<vector<int>> adj(n+1);
    vector<int> vis(n+1);  

    for (auto it : edges) {
        adj[it[1]].push_back(it[0]);
        adj[it[0]].push_back(it[1]);
    }

    for (int i = 0; i < n; ++i) {
        if (!vis[i]) {
            if (bfs(i, adj, vis)) {
                return "Yes";
            }
        }
    }

    return "No";
}
