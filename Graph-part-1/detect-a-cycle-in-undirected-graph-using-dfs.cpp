
bool dfs(int node, int parent, vector<int> &vis, vector<vector<int>> &adj){
    vis[node] = 2;

    for(int it: adj[node]){
        if(!vis[it]){
            if(dfs(it, node, vis, adj))return true;
        }
        else if(vis[it] == 2 && it != parent)return true;
    }

    return false;
}


string cycleDetection (vector<vector<int>>& edges, int n, int m)
{
    vector<vector<int>> adj(n+1);
    vector<int> vis(n+1);
    for(auto it: edges){
        adj[it[0]].push_back(it[1]);
        adj[it[1]].push_back(it[0]);
    }

    for(int i=1; i<=n; ++i){
        if(!vis[i]){
            if(dfs(i, -1, vis, adj))return "Yes";
        }
    }

    return "No";
}
