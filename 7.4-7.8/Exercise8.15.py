#coding:gb2312
#�����ض��ĺ���
"""
from fuzhu import make_pizza
make_pizza(16,'mushrooms')
make_pizza(24,'a','s','d','v')
"""
#ʹ��as�������ƶ�����
"""
from fuzhu import make_pizza as mp
mp(16,'mushrooms')
mp(24,'a','s','d','v')
"""
#ʹ��as��ģ��ָ������
"""
import fuzhu as f
f.make_pizza(16,'mushrooms')
f.make_pizza(24,'a','s','d','v')
"""
#����ģ���е����к���

from fuzhu import *
make_pizza(16,'mushrooms')
make_pizza(24,'a','s','d','v')
