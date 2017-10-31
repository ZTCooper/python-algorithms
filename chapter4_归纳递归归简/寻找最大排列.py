#	 a  b  c  d  e  f  g  h
M = [2, 2, 0, 5, 3, 5, 7, 4]
#	 c  c  a  f  d  f  h  e

#寻找最大排列问题的递归算法思路的朴素实现方案
def naive_max_perm(M, A = None):
	if A is None:
		A = set(range(len(M)))
	if len(A) == 1:
		return A
	B = set(M[i] for i in A)
	C = A - B
	if C:
		A.remove(C.pop())
		return naive_max_perm(M, A)
	return A
