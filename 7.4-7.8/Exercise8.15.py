#coding:gb2312
#导入特定的函数
"""
from fuzhu import make_pizza
make_pizza(16,'mushrooms')
make_pizza(24,'a','s','d','v')
"""
#使用as给函数制定别名
"""
from fuzhu import make_pizza as mp
mp(16,'mushrooms')
mp(24,'a','s','d','v')
"""
#使用as给模块指定别名
"""
import fuzhu as f
f.make_pizza(16,'mushrooms')
f.make_pizza(24,'a','s','d','v')
"""
#导入模块中的所有函数

from fuzhu import *
make_pizza(16,'mushrooms')
make_pizza(24,'a','s','d','v')
