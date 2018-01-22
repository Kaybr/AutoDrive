# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 01:19:34 2017

@author: satyanarayan pande
"""

import cv2

def draw_lines(img, lines):
    try:
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(img, (x1, y1), (x2, y2), [0, 255, 255], 3)
    except Exception as e:
        print(str(e) + "In lines_Correction")
        pass