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


G2 = {
	0:{1, 2},
	1:{0, 2},
	2:{0, 1},
	3:{4, 5},
	4:{3, 5},
	5:{3, 4}
}

#找出图的连通分量
def components(G):
	comp = []			#components
	seen = set()		#nodes already seen
	for u in G:			
		if u in seen:
			continue
		C = walk(G, u)	#traverse component
		#print(C)
		seen.update(C)	#add keys of C to seen
		comp.append(C)	#add one component
	#print(comp)
	return comp

if __name__ == "__main__":
	print(list(walk(G1, a)))	#traversal tree -> list
	print([list(sorted(C)) for C in components(G2)])	#dict -> list
	
