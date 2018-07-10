#coding:gb2312
#习题1
#import module_name
"""
print("\n\n习题1:")
import fuzhu
fuzhu.make_pizza(16,'mushrooms')
fuzhu.make_pizza(24,'a','s','d','v')
"""
#import module_name import function_name
"""
import fuzhu
from fuzhu import make_pizza
make_pizza(16,'mushrooms')
make_pizza(24,'a','s','d','v')
"""
#import module_name import function_name as mp
"""
import fuzhu
from fuzhu import make_pizza as mp
mp(16,'mushrooms')
mp(24,'a','s','d','v')
"""
#import module_name as fz
"""
import fuzhu as fz
fz.make_pizza(16,'mushrooms')
fz.make_pizza(24,'a','s','d','v')
"""
#import module_name import *
import fuzhu
from fuzhu import *
make_pizza(16,'mushrooms')
make_pizza(24,'a','s','d','v')
