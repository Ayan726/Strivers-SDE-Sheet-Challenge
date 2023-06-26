class Solution {
private:
    vector<int> vis;
    bool dfs(int node, vector<vector<int>> &adj){
        vis[node] = 2;

        for(int it: adj[node]){
        if(!vis[it]){
            if(dfs(it, adj))return true;
        }
        else if(vis[it] == 2)return true;
        }

        vis[node] = 1;

        return false;
    }
public:
    bool canFinish(int n, vector<vector<int>>& prq) {
        vector<vector<int>> adj(n);
        for(auto it: prq){
            adj[it[1]].push_back(it[0]);
        }

        vis.resize(n);

        for(int i=0; i<n; ++i){
            if(!vis[i]){
                if(dfs(i, adj))return false;
            }
        }

        return true;
    }
};
