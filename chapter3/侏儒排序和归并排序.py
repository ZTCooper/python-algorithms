#侏儒排序（稳定）
def gnomesort(seq):
	i = 0
	while i < len(seq):
		if i == 0 or seq[i - 1] <= seq[i]:
			i += 1
		else:
			seq[i], seq[i - 1] = seq[i - 1], seq[i]
			i -= 1
	return seq

#归并排序
def mergesort(seq):
	mid = len(seq)//2
	lft, rgt = seq[:mid], seq[mid:]
	if len(lft) > 1:
		lft = mergesort(lft)
	if len(rgt) > 1:
		rgt = mergesort(rgt)
	res = []
	while lft and rgt:
		if lft[-1] > rgt[-1]:
			res.append(lft.pop())
		else:
			res.append(rgt.pop())
	res.reverse()
	return (lft or rgt) + res

#几乎已排好序选择侏儒，一般情况选择归并
