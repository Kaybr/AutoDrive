# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 21:07:58 2017

@author: satyanarayan pande
"""
import numpy as np
import cv2

def roi(img, vertices):
    mask = np.zeros_like(img)
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
    
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked = cv2.bitwise_and(img, mask)
    
    return masked

