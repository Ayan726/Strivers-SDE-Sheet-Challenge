class Solution
{
	public:
	//Function to return list containing vertices in Topological order. 
	vector<int> topoSort(int n, vector<int> adj[]) 
	{
	    int indegree[n] = {0};
	    
	    for(int i=0; i<n; ++i){
	        for(int it: adj[i]){
	            indegree[it]++;
	        }
	    }
	    
	    queue<int> q;
	    for(int i=0; i<n; ++i){
	        if(!indegree[i])q.push(i);
	    }
	    vector<int> res;
	    while(!q.empty()){
	        int f = q.front();
	        q.pop();
	        res.push_back(f);
	        for(int it: adj[f]){
	            indegree[it]--;
	            if(!indegree[it]){
	                q.push(it);
	            }
	        }
	    }
	    
	    return res;
	    
	}
};
