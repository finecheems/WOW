import cv2 as cv
import numpy as np
def blur(image):
    example=input('请输入一个大于一的数以调整虚化度(5的效果最好)')
    image = cv.imread('tmp.png')
    dst = cv.blur(image, (int(example),int( example)))
    return dst
background = blur(cv.imread('tmp.png'))
img = cv.imread('tmp.png')
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (30,60,310,340)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,11,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
combine = cv.addWeighted(cv.resize(img,(0, 0), fx=1.0, fy=1.0, interpolation=cv.INTER_NEAREST),0.2,cv.resize(background,(0, 0), fx=1.0, fy=1.0, interpolation=cv.INTER_NEAREST),0.8,0)
combine_2 = cv.addWeighted(cv.resize(img,(0, 0), fx=1.0, fy=1.0, interpolation=cv.INTER_NEAREST),0.4,cv.resize(combine,(0, 0), fx=1.0, fy=1.0, interpolation=cv.INTER_NEAREST),0.8,0)
combine-=img
cv.imshow('combine',combine_2)
cv.imwrite('task-8.png',combine)
cv.waitKey(0)