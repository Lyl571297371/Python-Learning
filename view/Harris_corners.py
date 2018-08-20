from pylab import *
from numpy import *
from PIL import Image
import harris


# 打开图片
im = array(Image.open('C://Users//HASEE//Desktop//empire.jpg').convert('L'))

# 检测拐角并绘制
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim, 10, threshold=0.01)
harris.plot_harris_points(im, filtered_coords)

# 只画200个最优的
harris.plot_harris_points(im, filtered_coords[:200])
