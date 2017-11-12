G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}
#[a, b, c, d, e, f]

#朴素版的拓扑排序法（平方级）
def naive_topsort(G, S = None):
	if S is None:
		S = set(G)				#all nodes
	if len(S) == 1:				#single node
		return list(S)			
	v = S.pop()					#Reduction: remove a node
	seq = naive_topsort(G, S)	#Recursion(assumption), n-1
	min_i = 0
	for i, u in enumerate(seq):
		if v in G[u]:
			min_i = i + 1		#after all dependencies
	seq.insert(min_i, v)
	return seq

#有向无环路图DAG(Directed Acyclic Graph)的拓扑排序
#删除无入度的点
def topsort(G):
	count = dict((u, 0) for u in G)	
	#{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
	for u in G:
		for v in G[u]:
			count[v] += 1		#in_degree
	Q = [u for u in G if count[u] == 0]		#nodes with no in_degree
	S = []		#result
	while Q:
		u = Q.pop()
		S.append(u)
		for v in G[u]:
			count[v] -= 1		#uncount out_degree
			if count[v] == 0:	#new node without in_degree
				Q.append(v)
	return S

if __name__ == "__main__":
	print(naive_topsort(G))
	print(topsort(G))
