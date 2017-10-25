#递归插入排序
def ins_sort_rec(seq, i):
	if i == 0:
		return
	ins_sort_rec(seq, i-1)		#对0到i-1排序
	j = i
	while j > 0 and seq[j - 1] > seq[j]:		#寻找插入位置
		seq[j-1], seq[j] = seq[j], seq[j-1]
		j -= 1
	return seq

#插入排序
def ins_sort(seq):
	for i in range(len(seq)):
		j = i
		while j > 0 and seq[j-1] > seq[j]:
			seq[j-1], seq[j] = seq[j], seq[j-1]
			j -= 1
	return seq

#递归选择排序
def sel_sort_rec(seq, i):
	if i == 0:
		return
	max_j = i
	for j in range(i):		#寻找最大值
		if seq[j] > seq[max_j]:
			max_j = j 		#update max_j
	seq[i], seq[max_j] = seq[max_j], seq[i]
	sel_sort_rec(seq, i-1)
	return seq

#选择排序
def sel_sort(seq):
	for i in range(len(seq)-1,0,-1):
		max_j = i
		for j in range(i):
			if seq[j] > seq[max_j]:
				max_j = j
		seq[i], seq[max_j] = seq[max_j], seq[i]
	return seq
