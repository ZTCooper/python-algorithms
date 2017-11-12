>>> L = [randrange(10000) for i in range(1000)]
>>> 42 in L		#成员查询在list中是线性级的
False
>>> S = set(L)	#在set中是常数级的
>>> 42 in S
False
#如果要依次往集合中添加新值并检测是否已经被添加
#list操作是平方级的
#set是线性级的


