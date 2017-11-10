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
		if [c][v]:				#candidate knows others
			break				
		if not G[v][c]:			#other doesn't know csndidate
			break
	else:						#no breaks
		return c 				#c is celebrity
	return None					#couldn't find anyone
