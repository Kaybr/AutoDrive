# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 20:17:30 2017

@author: satyanarayan pande
"""
import cv2
import numpy as np
from regionOfInterest import roi
from linesCorrection import draw_lines

def mod_process_img(original_img):
    
    gray_image = cv2.cvtColor(original_img, cv2.COLOR_RGB2GRAY)
    img_hsv = cv2.cvtColor(original_img, cv2.COLOR_RGB2HSV)
    
    lower_yellow = np.array([20,100,100], dtype = 'uint8')
    upper_yellow = np.array([30,255,255], dtype = 'uint8')
    mask_yellow = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
    mask_white = cv2.inRange(gray_image, 200, 255)
    mask_yw = cv2.bitwise_or(mask_white, mask_yellow)
    mask_yw_image = cv2.bitwise_and(gray_image, mask_yw)
    
    blurred_img = cv2.GaussianBlur(mask_yw_image, (5, 5), 0)
    
    canny_edge = cv2.Canny(blurred_img, 50, 150)
    
    imshape = original_img.shape
    lower_left = [imshape[1]/9, imshape[0]]
    lower_right = [imshape[1] - imshape[1]/9, imshape[0]]
    top_left = [imshape[1]/2 - imshape[1]/8, imshape[0]/2 + imshape[0]/10]
    top_right = [imshape[1]/2 + imshape[1]/8, imshape[0]/2 + imshape[0]/10]
    
    vertices = [np.array([lower_left, top_left, top_right, lower_right], dtype = np.int32)]
    roi_img = roi(canny_edge, vertices)
    
    lines = cv2.HoughLinesP(roi_img, 2, np.pi/180, 20, np.array([]), minLineLength =  50, maxLineGap = 200)
    line_img = np.zeros((roi_img.shape[0], roi_img.shape[1], 3), dtype = np.uint8)
    draw_lines(line_img, lines)
    
    return cv2.addWeighted(original_img, 0.8, line_img, 1.0, 0.0)
    
    