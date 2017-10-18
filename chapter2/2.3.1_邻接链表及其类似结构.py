#2-1 邻接集表示法
a, b, c, d, e, f, g, h = range(8)
N = [
	{b, c, d, e, f},	#a
	{c, e},				#b
	{d},				#c
	{e},				#d
	{f},				#e
	{c, g, h},			#f
	{f, h},				#g
	{f, g}				#h
]
#>>> b in N[a]	#Neighborhood membership
#True
#>>> len(N[f])	#Degree
#3


#2-2 邻接列表
a, b, c, d, e, f, g, h = range(8)
N = [
	[b, c, d, e, f],	#a
	[c, e],				#b
	[d],				#c
	[e],				#d
	[f],				#e
	[c, g, h],			#f
	[f, h],				#g
	[f, g]				#h
]
#可用列表最后一项覆盖要删除的对象，然后调用pop


#2-3 加权邻接字典
a, b, c, d, e, f, g, h = range(8)
N = [
	{b:2, c:1, d:3, e:9, f:4},	#a
	{c:4, e:3},					#b
	{d:8},						#c
	{e:7},						#d
	{f:5},						#e
	{c:2, g:2, h:2},			#f
	{f:1, h:6},					#g
	{f:9, g:8}					#h
]
#>>> b in N[a]		#Neighborhood membership
#True
#>>> len(N[f])		#Degree
#3
#>>>N[a][b]			#Edge weight for (a,b)
#2


#2-4 邻接集的字典表示法
N = {
	'a': set('bcdef'),
	'b': set('ce'),
	'c': set('d'),
	'd': set('e'),
	'e': set('f'),
	'f': set('cgh'),
	'g': set('fh'),
	'h': set('fg')
}


#2-5 邻接矩阵
a, b, c, d, e, f, g, h = range(8)
#	  a b c d e f g h
N = [[0,1,1,1,1,1,0,0],	#a
	 [0,0,1,0,1,0,0,0],	#b
	 [0,0,0,1,0,0,0,0],	#c
	 [0,0,0,0,1,0,0,0],	#d
	 [0,0,0,0,0,1,0,0],	#e
	 [0,0,1,0,0,0,1,1],	#f
	 [0,0,0,0,0,1,0,1],	#g
	 [0,0,0,0,0,1,1,0]]	#h
#>>> N[a][b]		#Neighborhood membership
#1
#>>> sum(N[f])		#Degree
#3


#2-6 对不存在的边赋予无限大的权值的加权矩阵
a, b, c, d, e, f, g, h = range(8)
inf = float('inf')		#sys.maxint
#		a    b    c    d    e    f    g    h
W = [[  0,   2,   1,   3,   9,   4, inf, inf],	#a
	 [inf,   0,   4, inf,   3, inf, inf, inf],	#b
	 [inf, inf,   0,   8, inf, inf, inf, inf],	#c
	 [inf, inf, inf,   0,   7, inf, inf, inf],	#d
	 [inf, inf, inf, inf,   0,   5, inf, inf],	#e
	 [inf, inf,   2, inf, inf,   0,   2,   2],	#f
	 [inf, inf, inf, inf, inf,   1,   0,   6],	#g
	 [inf, inf, inf, inf, inf,   9,   8,   0]]	#h
#>>> W[a][b] < inf		#Neighborhood membership
#True
#>>> W[c][e] < inf		#Neighborhood membership
#False
#>>> sum(1 for w in W[a] if w < inf) - 1	#Degree
#5
#这里记得-1，因为不算对角线！


#N = [[0]*10 for i in range(10)]
import Numpy as np
N = np.zeros([10, 10])