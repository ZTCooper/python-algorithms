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

def traverse(G, s, qtype = set):
	S, Q = set(), qtype()
	Q.add(s)
	while Q:
		u = Q.pop()
		if u in S:
			continue
		S.add(u)
		for v in G[u]:
			Q.add(v)
		yield u

if __name__ == "__main__":
	print(list(traverse(G, a)))
