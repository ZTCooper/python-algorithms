>>> 0.1
0.1
>>> sum(0.1 for i in range(10)) == 1.0
False
#不要对浮点数进行等值比较

>>> def almost_equal(x, y, places = 7):		#保留7位小数
...     return round(abs(x - y), places) == 0		#round()四舍五入，保留places位小数
...
>>> almost_equal(sum(0.1 for i in range(10)), 1.0)
True

#如需要某种精确的十进制浮点数表示法
>>> from decimal import *
>>> sum(Decimal('0.1') for i in range(10)) == Decimal('1.0')
True

#两个接近等值的子表达式相减，通常会丢失大量有效数字
>>> from math import sqrt
>>> x = 8762348761.13
>>> sqrt(x + 1) - sqrt(x)
5.341455107554793e-06
>>> 1.0/(sqrt(x + 1) + sqrt(x))		#有理化
5.3414570026237696e-06
