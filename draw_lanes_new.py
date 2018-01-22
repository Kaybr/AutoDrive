# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 01:19:34 2017

@author: satyanarayan pande
"""
from numpy import ones, vstack
from numpy.linalg import lstsq
from statistics import mean

def draw_lanes(img, lines, color = [0, 255, 255], thickness = 3):
    try:
        y = []
        for line in lines:
            for i in line:
                y = y + [i[1], i[3]]
        
        min_y = min(y)
        max_y = 600
        #new_lines = []
        line_dict = {}
        
        for index, i in enumerate(lines):
            for xy in i:
                x = (xy[0], xy[2])
                y = (xy[1], xy[3])
                A = vstack([x, ones(len(x))]).T
                m, b = lstsq(A, y)[0]
                
                x1 = (min_y - b) / m
                x2 = (max_y - b) / m
                
                line_dict[index] = [m, b, [int(x1), min_y, int(x2), max_y]]
                #new_lines.append([int(x1), min_y, int(x2), max_y])
                
        final_lanes = {}
        
        for index in line_dict:
            final_lanes_copy = final_lanes.copy()
            m = line_dict[index][0]
            b = line_dict[index][1]
            line = line_dict[index][2]
            
            if len(final_lanes) == 0:
                final_lanes[m] = [[m , b, line]]
            else:
                found_copy = False
                
                for other_ms in final_lanes_copy:
                    
                    if not found_copy:
                        if abs(other_ms * 1.4) > abs(m) > abs(other_ms * 0.6):
                            if abs(final_lanes_copy[other_ms][0][1] * 1.4) > abs(b) > abs(final_lanes_copy[other_ms][0][1] * 0.6):
                                final_lanes[other_ms].append([m, b, line])
                                found_copy = True
                                break
                        else:
                            final_lanes[m] = [[m, b, line]]
                                
        line_counter = {}
        
        for lanes in final_lanes:
            line_counter[lanes] = len(final_lanes[lanes])
            
        top_lanes = sorted(line_counter.items(), key = lambda item: item[1])[::-1][:2]
        
        lane1_id = top_lanes[0][0]
        lane2_id = top_lanes[1][0]
        
        def average_lane(lane_data):
            x1 = []
            y1 = []
            x2 = []
            y2 = []
            
            for data in lane_data:
                x1.append(data[2][0])
                y1.append(data[2][1])
                x2.append(data[2][2])
                y2.append(data[2][3])
                
            return int(mean(x1)), int(mean(y1)), int(mean(x2)), int(mean(y2))
                                     
        l1_x1, l1_y1, l1_x2, l1_y2 = average_lane(final_lanes[lane1_id])
        l2_x1, l2_y1, l2_x2, l2_y2 = average_lane(final_lanes[lane2_id])
        
        return [l1_x1, l1_y1, l1_x2, l1_y2], [l2_x1, l2_y1, l2_x2, l2_y2]
    
    except Exception as e:
        print(str(e) + "In draw_lanes")
    