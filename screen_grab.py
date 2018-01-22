# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 20:17:30 2017

@author: satyanarayan pande
"""
import numpy as np
from PIL import ImageGrab
import cv2
import time
#from modified_process_img import mod_process_img
from process_img import process_img
#from directKeys import PressKey,ReleaseKey, W#, S, A, D

def main():
    last_time = time.time()
    while(True):
        screen = np.array(ImageGrab.grab(bbox = (0,40,800,640)))
    #screen = cv2.imread('sample_three.jpg')
        new_screen,original_img = process_img(screen)
        
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        
        cv2.imshow('New Screen', new_screen)
        cv2.imshow('Original Image', cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        
    #cv2.waitKey(0)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
main()