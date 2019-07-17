# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:32:16 2019

@author: Mehmet YEŞİLKAYA
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    canny = cv2.Canny(frame, 20, 100)
    cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('canny',canny)
    k = cv2.waitKey(5) & 0xFF
    #ESC
    if k ==27:
        break
    
cv2.destroyAllWindows()
cap.release()    

