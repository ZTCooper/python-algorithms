#	 a  b  c  d  e  f  g  h
M = [2, 2, 0, 5, 3, 5, 7, 4]
#	 c  c  a  f  d  f  h  e

#寻找最大排列问题的递归算法思路的朴素实现方案
def naive_max_perm(M, A = None):
	if A is None:
		A = set(range(len(M)))	#A = {0,1,...,n-1}
	if len(A) == 1:
		return A
	B = set(M[i] for i in A)	#有入度的点集
	C = A - B  					#删除有入度的点，C为无入度的点集
	if C:
		A.remove(C.pop())		#删除其中一个无入度点
		return naive_max_perm(M, A)		#handle remaining elements
	return A
#时间复杂度平方级

#迭代实现
def max_perm(M):
	n = len(M)
	A = set(range(n))		#A = {0,1,...,n-1}
	count = [0]*n 			#count = [0,0,...,0]
	for i in M:
		count[i] += 1		#入度
	Q = [i for i in A if count[i] == 0]		#无入度的点集
	while Q:
		i = Q.pop()			#get one
		A.remove(i)			#remove it from A
		j = M[i]			#同时删除其指向的点
		count[j] -= 1		#被指向点的入度-1
		if count[j] == 0:	#如果j此时无入度
			Q.append(j)		#deal with j
	return A
#算法复杂度：线性级

if __name__ == "__main__":
	print(naive_max_perm(M))
	print(max_perm(M))
