# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 20:17:30 2017

@author: satyanarayan pande
"""
import cv2
import numpy as np

def mod_canny(image, sigma):
    
    v = np.median(image)
    
    lower = int(max(0, (2.0 - sigma) * v))
    upper = int(min(255, (2.0 + sigma) * v))
    processed_img = cv2.Canny(image, 200, 300)
    
    return processed_img