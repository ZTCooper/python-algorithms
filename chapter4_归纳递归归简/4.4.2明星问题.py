#构造随机图
from random import randrange
n = 1000
G = [[randrange(2) for i in range(n)] for i in range(n)]
#randrange(2) -> 0 or 1
#[[0, ..., 1], [0, ..., 0], ..., [0, ..., 1]]

#指定明星
c = randrange(n)	#one in 0-999
for i in range(n):
	G[i][c] = True		#others know c
	G[c][i] = False		#c doesn't know others

#朴素版的明星问题方案
def naive_celeb(G):
	n = len(G)
	for u in range(n):			#candidate
		for v in range(n):		#everyone else
			if u == v:			#same person, skip
				continue
			if G[u][v]:			#candidate knows other
				break
			if not G[v][u]:		#other doesn't know candidate
				break
		else:
			return u			#no break, is Celebrity
	return None					#couldn't find anyone

#明星问题的解决方案
#要么此人认识其他人，要么谁也不认识此人
def celeb(G):
	n = len(G)
	u,v = 0,1					#the first two
	for c in range(2, n + 1):	#others to check
		if G[u][v]:				#u knows v
			u = c  				#replace u with c
		else:					#u doesn't know v
			v = c 				#replace v
	if u == n:					#u was replaced last
		c = v					#use v
	else:						#otherwise
		c = u 					#u is a candidate
	for v in range(n):			#for everyone else
		if c == v:				#same person
			continue			#skip
		if G[c][v]:				#candidate knows others
			break				
		if not G[v][c]:			#other doesn't know csndidate
			break
	else:						#no breaks
		return c 				#c is celebrity
	return None					#couldn't find anyone

if __name__ == '__main__':
	print(naive_celeb(G))
	print(celeb(G))
