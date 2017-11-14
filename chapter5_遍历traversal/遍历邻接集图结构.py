a, b, c, d, e, f, g, h = range(8)
G1 = [
	{b, c, d, e, f},	#a
	{c, e},				#b
	{d},				#c
	{e},				#d
	{f},				#e
	{c, g, h},			#f
	{f, h},				#g
	{f, g}				#h
]

#遍历一个表示为邻接集的图结构的连通分量
def walk(G, s, S = set()):		#walk graph G from node s
	P, Q = dict(), set()		#predecessors + "to do" queue(前驱和后继)
	P[s] = None					#s has no predecessor
	Q.add(s)					#plan on starting with s
	while Q:					#还有没visit过的点
		u = Q.pop()				#get one
		for v in G[u].difference(P, S):		#G[u]中有，但P,S中没有的元素
											#new nodes
			Q.add(v)			#plan to visit them
			P[v] = u			#predecessor of v
	return P 					#trversal tree

if __name__ == "__main__":
	print(list(walk(G1, a)))	#traversal tree -> list
	
