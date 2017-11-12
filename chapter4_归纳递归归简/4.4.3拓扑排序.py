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

if __name__ == "__main__":
	print(naive_topsort(G))
