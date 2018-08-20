from pylab import *
from numpy import *
from PIL import Image
import harris
import imresize



im1 = array(Image.open("C://Users//HASEE//Desktop//crans_1_small.jpg").convert("L"))
im2 = array(Image.open("C://Users//HASEE//Desktop//crans_2_small.jpg").convert("L"))

# 调整大小加快匹配速度
im1 = imresize(im1,(im1.shape[1]//2,im1.shape[0]//2))
im2 = imresize(im2,(im2.shape[1]//2,im2.shape[0]//2))#书种版本较旧  此处应为两个//

wid = 5
harrisim = harris.compute_harris_response(im1,5) 
filtered_coords1 = harris.get_harris_points(harrisim,wid+1) 
d1 = harris.get_descriptors(im1,filtered_coords1,wid)

harrisim = harris.compute_harris_response(im2,5) 
filtered_coords2 = harris.get_harris_points(harrisim,wid+1) 
d2 = harris.get_descriptors(im2,filtered_coords2,wid)

print ('starting matching')
matches = harris.match_twosided(d1,d2)

figure()
gray() 
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches) 
show()
