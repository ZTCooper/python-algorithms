#二维列表(lists of lists)
T = [['a', 'b'], ['c'], ['d', ['e', 'f']]]
#>>> T[0][1]
#'b'
#>>> T[2][1][0]
#'e'


#2-7 二叉树类
class Tree:
	def __init__(self, left, right):
		self.left = left
		self.right = right
#>>> t = Tree(Tree('a','b'), Tree('c','d'))
#>>> t.right.lrft
#'c'


#2-8 多路搜索树类（孩子兄弟）
class Tree:
	def __init__(self, kids, next=None):
		self.kids = self.val = kids
		self.next = next
#>>> t = Tree(Tree('a', Tree('b',Tree('c', Tree('d')))))
#>>> t.kids.next.next.val
#'c'


#Bunch模式
class Bunch(dict):
	def __init__(self, *args, **kwds):
		super(Bunch, self).__init__(*args, **kwds)
		self.__dict__ = self
#>>> x = Bunch(name = 'Jayne Cobb', position = 'Public Relations')
#>>> x.name
#'Jayne Cobb'
#继承于dict类
#>>> T = Bunch
#>>> t = T(left = T(left = 'a', right = 'b'), right = T(left = 'c'))
#>>> t.left
#{'right':'b', 'left':'a'}
#>>> t.left.right
#'b'
#>>> t['left']['right']
#'b'
#>>> 'left' in t.right
#True
#>>> 'right' in t.right
#False