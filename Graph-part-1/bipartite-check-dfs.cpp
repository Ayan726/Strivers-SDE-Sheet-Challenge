bool dfs(int node, int col, vector<vector<int>> &adj, vector<int> &color){
	color[node] = col;

	for(int it: adj[node]){
		if(color[it] == color[node])return false;
		else if(color[it] == -1){
			if(!dfs(it, !col, adj, color))return false;
		}
	}

	return true;
}

bool isGraphBirpatite(vector<vector<int>> &edges) {
	vector<vector<int>> adj(edges.size());
	vector<int> color(edges.size(), -1);

	for(int i=0; i<edges.size(); ++i){
		for(int j=0; j<edges.size(); ++j){
			if(edges[i][j]){
				adj[i].push_back(j);
				adj[j].push_back(i);
			}
		}
	}

	for(int i=0; i<adj.size(); ++i){
		if(color[i] == -1){
			if(!dfs(i, 0, adj, color))return false;
		}
	}

	return true;
}
