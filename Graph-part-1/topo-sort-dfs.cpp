class Solution
{   private:
    vector<int> vis;
    vector<int> res;
    void dfs(int node, vector<int> adj[]){
        vis[node] = 1;
        
        for(int it: adj[node]){
            if(!vis[it])dfs(it, adj);
        }
        res.push_back(node);
        
    }
	public:
	//Function to return list containing vertices in Topological order. 
	vector<int> topoSort(int n, vector<int> adj[]) 
	{
	    vis.resize(n);
	    for(int i=0; i<n; ++i){
	        if(!vis[i])dfs(i, adj);
	    }
	    reverse(res.begin(), res.end());
	    return res;
	    
	}
};
