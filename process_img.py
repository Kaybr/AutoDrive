# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 20:17:30 2017

@author: satyanarayan pande
"""
import cv2
import numpy as np
from regionOfInterest import roi
from modified_canny import mod_canny
from draw_lanes_new import draw_lanes

def process_img(image):
    original_img = image
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    processed_img = mod_canny(processed_img, sigma = 0.5)
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)
    vertices = np.array([[0,600], [0, 500], [350,320], [400,320], [800, 500], [800,600]], np.int32)
    processed_img = roi(processed_img, [vertices])
    
    #lines = cv2.HoughLinesP(processed_img, 5, np.pi/180, 180, 5, 200)
    lines = cv2.HoughLinesP(processed_img, 2, np.pi/180, 20, np.array([]), 50, 200)
    
    try:
        l1, l2 = draw_lanes(original_img, lines)
        original_img = cv2.line(original_img, (l1[0], l1[1]), (l1[2], l1[3]), [0, 255, 0], 30)
        original_img = cv2.line(original_img, (l2[0], l2[1]), (l2[2], l2[3]), [0, 255, 0], 30)
    except Exception as e:
        print(str(e) + "After the houghlines")
        pass
    
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 0, 0], 3)
                
            except Exception as e:
                print(str(e) + "In coords section in process_img")
                
    except Exception as e:
        print(str(e) + "Unable to find the lines:")
        pass
    
    return processed_img, original_img