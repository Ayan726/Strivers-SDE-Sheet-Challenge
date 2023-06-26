class Solution {
public:
    bool canFinish(int n, vector<vector<int>>& prq) {
        vector<int> indegree(n);
        vector<vector<int>> adj(n);
        for(auto it: prq){
            indegree[it[0]]++;
            adj[it[1]].push_back(it[0]);
        }
        queue<int> q;
        for(int i=0; i<indegree.size(); ++i){
            if(!indegree[i])q.push(i);
        }
        int cnt = 0;
        while(!q.empty()){
            int f = q.front();
            q.pop();
            ++cnt;

            for(int it:adj[f]){
                indegree[it]--;
                if(!indegree[it])q.push(it);
            }
        }

        return cnt==n;
    }
};
