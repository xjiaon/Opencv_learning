# -*- coding: cp936 -*-
'''
#我女儿喜欢看小马宝莉，也喜欢给简笔画涂色彩
#我这个脚本就是给她写的， 随意找张动画片屏幕截图， 就可以制成简笔画了
#用法python pan_painting.py -i 你的图片 例如 python pan_painting.py -y time.jpg
#此脚本是windows环境python 2.7+opencv3.2版本的
#需要提前安装speech模块， 安装方法pip install speech
'''
print (__doc__)
import cv2
#导入cv2这个module模块
import numpy as np
#导入numpy这个计算用的模块
import argparse
#导入参数模块
import speech
#加载语音模块
speech.say("现在开始")
#说话， 代表开始
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
#提示需要加入图片的提示
args = vars(ap.parse_args())
#这个就是会代入程序的图片名称参数值

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
im = cv2.imread(args["image"])
#读取命令中代入的图片名称
kernel = np.ones((5,5),np.uint8)
#im=cv2.imread('time.jpg',0)

cv2.imshow('1',im)
#显示这个图片
ret, thresh=cv2.threshold(im,150,255,cv2.THRESH_BINARY_INV)
#黑白差值化
cv2.imshow('thresh',thresh)
#显示黑白差值图
edges = cv2.Canny(im,0,255,3)
#这个是边缘图，黑底，白线
edges_INV =cv2.bitwise_not(edges)
#取反， 白底，黑线
#erosion = cv2.erode(edges1,kernel,iterations = 1)
#dilation = cv2.dilate(edges1,kernel,iterations = 1)
cv2.imwrite(args["image"],edges_INV)
#写入源文件， 替换掉原图
cv2.imshow('2',edges_INV)

#显示新图
#cv2.imshow('erosion',erosion)
#cv2.imshow('dilation',dilation)
speech.say("转换结束")
#语音提示， 提示程序完成
cv2.waitKey(0)
#按任意键退出

