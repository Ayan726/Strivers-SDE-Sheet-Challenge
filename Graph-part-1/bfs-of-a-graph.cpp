class Solution {
  public:
    // Function to return Breadth First Traversal of given graph.
    vector<int> bfsOfGraph(int v, vector<int> adj[]) {
        int vis[v] = {0};
        queue<int> q;
        q.push(0);
        vis[0] = 1;
        vector<int> res;
        while(!q.empty()){
            int f = q.front();
            q.pop();
            res.push_back(f);
            
            for(auto it:adj[f]){
                if(!vis[it])q.push(it),vis[it] = 1;
                
            }
        }
        
        return res;
    }
};
