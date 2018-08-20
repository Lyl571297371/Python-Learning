#coding:gb2312
from PIL import Image
import os
from numpy import *
from pylab import *


def process_image(imagename,resultname,params="--edge-thresh 10 --peak-thresh 5"):
    """ ����һ��ͼ��Ȼ�󽫽���������ļ��� """

    if imagename[-3:] != 'pgm':
        # ����һ��pgm�ļ�
        im = Image.open(imagename).convert('L')
        im.save('tmp.pgm')
        imagename = 'tmp.pgm'

    cmmd = str("C:\\Program Files\\Anaconda3\\Lib\\site-packages\\win64vlfeat\\sift.exe"+imagename+" --output="+resultname+
                " "+params)
    os.system(cmmd)
    print ('processed', imagename, 'to', resultname)


def read_features_from_file(filename):
    """ ��ȡ��������ֵ��Ȼ�����Ծ�����ʱ���� """
    
    f = loadtxt(filename)
    return f[:,:4],f[:,4:] # ����λ��������


def write_features_to_file(filename,locs,desc):
    """ ������λ�ú������ӱ��浽�ļ��� """
    savetxt(filename,hstack((locs,desc)))
    

def plot_features(im,locs,circle=False):
    """ ��ʾ����������ͼ��
		input: im (����ͼ��), 
        locs (��,��, �߶Ⱥͷ���Ƕ�). """

    def draw_circle(c,r):
        t = arange(0,1.01,.01)*2*pi
        x = r*cos(t) + c[0]
        y = r*sin(t) + c[1]
        plot(x,y,'b',linewidth=2)

    imshow(im)
    if circle:
        for p in locs:
            draw_circle(p[:2],p[2]) 
    else:
        plot(locs[:,0],locs[:,1],'ob')
    axis('off')


def match(desc1,desc2):
    """ ���ڵ�һ��ͼ���е�ÿ�������ӣ�ѡȡ�ڵڶ���ͼ���е�ƥ��
        input: desc1 (��һ��ͼ���������), 
        desc2 (�ڶ���ͼ���������) """
    
    desc1 = array([d/linalg.norm(d) for d in desc1])
    desc2 = array([d/linalg.norm(d) for d in desc2])
    
    dist_ratio = 0.6
    desc1_size = desc1.shape
    
    matchscores = zeros((desc1_size[0]),'int')
    desc2t = desc2.T # Ԥ�ȼ������ת��
    for i in range(desc1_size[0]):
        dotprods = dot(desc1[i,:],desc2t) # �������
        dotprods = 0.9999*dotprods
        # �����Һͷ����򣬷��صڶ���ͼ��������������
        indx = argsort(arccos(dotprods))
        
        # �������ڵĽǶ��Ƿ�С��dist_ratio���Եڶ����ڵĽǶ�
        if arccos(dotprods)[indx[0]] < dist_ratio * arccos(dotprods)[indx[1]]:
            matchscores[i] = int(indx[0])
    
    return matchscores


def appendimages(im1,im2):
    """ ���ؽ�����ͼ�������ӳ�һ����ͼ�� """
    
    # ѡȡ��������������ͼ��Ȼ������㹻�Ŀ���
    rows1 = im1.shape[0]    
    rows2 = im2.shape[0]
    
    if rows1 < rows2:
        im1 = concatenate((im1,zeros((rows2-rows1,im1.shape[1]))), axis=0)
    elif rows1 > rows2:
        im2 = concatenate((im2,zeros((rows1-rows2,im2.shape[1]))), axis=0)
    # �����Щ�����û�У���ô���ǵ�������ͬ������Ҫ�������
    
    return concatenate((im1,im2), axis=1)


def plot_matches(im1,im2,locs1,locs2,matchscores,show_below=True):
    """ ��ʾһ����������ƥ��֮�����ߵ�ͼƬ
        input: im1,im2 (����ͼ��), locs1,locs2 (����λ��), 
        matchscores (match()�����), show_below (���ͼ��Ӧ����ʾ��ƥ����·�). """
    
    im3 = appendimages(im1,im2)
    if show_below:
        im3 = vstack((im3,im3))
    
    # show image
    imshow(im3)
    
    # draw lines for matches
    cols1 = im1.shape[1]
    for i,m in enumerate(matchscores):
        if m>0:
            plot([locs1[i][1],locs2[m][1]+cols1],[locs1[i][0],locs2[m][0]],'c')
    axis('off')


def match_twosided(desc1,desc2):
    """ ˫��Գư汾��match"""
    
    matches_12 = match(desc1,desc2)
    matches_21 = match(desc2,desc1)
    
    ndx_12 = matches_12.nonzero()[0]
    
    # ȥ�����ԳƵ�ƥ��
    for n in ndx_12:
        if matches_21[int(matches_12[n])] != n:
            matches_12[n] = 0
    
    return matches_12



