# -*- coding: utf-8 -*- 
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
w = 150
h = 150 
template = np.zeros((w, h), np.uint8)
for j in range(50):
    for i in range(50):
        template[i, j] = 200
       

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
while(1):
# 获取每一帧
    ret,frame=cap.read()  # 有可能读帧失败， ret==false 后面程序出错。
# 转换到HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
# 设定蓝色的阈值
    lower_blue=np.array([55,25,25])
    upper_blue=np.array([130,255,255])
# 根据阈值构建掩模
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    
    # All the 6 methods for comparison in a list
    for meth in methods:
#exec 语句用来执行储存在字符串或文件中的 Python 语句。
# 例如，我们可以在运行时生成一个包含 Python 代码的字符串，然后使用 exec 语句执行这些语句。
#eval 语句用来计算存储在字符串中的有效 Python 表达式
        method = eval(meth)
# Apply template Matching
        res = cv2.matchTemplate(mask,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# 使用不同的比较方法，对结果的解释不同
# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(frame,top_left, bottom_right, 255, 2)

# 对原图像和掩模进行位运算
    res=cv2.bitwise_and(frame,frame,mask=mask)
# 显示图像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
# 关闭窗口
cv2.destroyAllWindows()
