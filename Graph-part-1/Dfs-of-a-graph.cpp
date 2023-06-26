class solution{
private:
  vector<int> res, vis;
    void dfs(int node, vector<int> adj[]){
        vis[node] = 1;
        res.push_back(node);
        for(int it: adj[node]){
            if(!vis[it])dfs(it, adj);
        }
    }
  public:
    // Function to return a list containing the DFS traversal of the graph.
    vector<int> dfsOfGraph(int v, vector<int> adj[]) {
        vis.resize(v);
        for(int i=0; i<v; ++i){
            if(!vis[i])dfs(i, adj);
        }
        
        return res;
    }
};
