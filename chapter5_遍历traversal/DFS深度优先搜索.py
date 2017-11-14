#Depth-First-Search 

a, b, c, d, e, f, g, h = range(8)
G = [
	{b, c, d, e, f},	#a
	{c, e},				#b
	{d},				#c
	{e},				#d
	{f},				#e
	{c, g, h},			#f
	{f, h},				#g
	{f, g}				#h
]
#递归版的深度优先搜索
def rec_dfs(G, s, S = None):	#search from s
	if S is None:
		S = set()
	S.add(s)		#已访问过s
	for u in G[s]:		#neighbors of s
		if u in S:		#visited
			continue	#skip
		rec_dfs(G, u, S)		#new search from u
	return S

if __name__ == "__main__":
	print(list(rec_dfs(G, 0)))
