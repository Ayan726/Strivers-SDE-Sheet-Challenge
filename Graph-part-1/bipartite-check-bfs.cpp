class Solution {
private:
    vector<int> color;
    bool bfs(int node, vector<vector<int>> &adj){
        queue<int> q;
        q.push(node);
        color[node] = 0;

        while(!q.empty()){
            int f = q.front();
            q.pop();

            for(int it:adj[f]){
                if(color[it] == color[f])return false;
                else if(color[it] == -1){
                    q.push(it);
                    color[it] = !color[f];
                }
            }
        }

        return true;
    }
public:
    bool isBipartite(vector<vector<int>>& graph) {
        color.resize(graph.size(), -1);

        for(int i=0; i<graph.size(); ++i){
            if(color[i] == -1){
                if(!bfs(i, graph))return false;
            }
        }

        return true;
    }
};
