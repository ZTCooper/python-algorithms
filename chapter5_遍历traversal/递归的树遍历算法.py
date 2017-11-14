def tree_walk(T, r):		#从根t开始遍历数T
	for u in T[r]:			#t的每个孩子
		tree_walk(T, u)		#继续遍历subtree
