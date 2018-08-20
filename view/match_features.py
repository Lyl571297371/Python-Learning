from pylab import *
from numpy import *
from PIL import Image

import sift

imname1 = 'C:\Users\HASEE\Desktop\climbing_1_small.jpg'
imname2 = 'C:\Users\HASEE\Desktop\climbing_2_small.jpg'

# 处理并将结果保存到文件中
sift.process_image(imname1, imname1+'.sift')
sift.process_image(imname2, imname2+'.sift')

# 读取特征进行匹配
l1,d1 = sift.read_features_from_file(imname1+'.sift')
l2,d2 = sift.read_features_from_file(imname2+'.sift')
matchscores = sift.match_twosided(d1, d2)

# 加载并会图
im1 = array(Image.open(imname1))
im2 = array(Image.open(imname2))

sift.plot_matches(im1,im2,l1,l2,matchscores,show_below=True)
show()
