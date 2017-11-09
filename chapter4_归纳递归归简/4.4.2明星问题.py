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
