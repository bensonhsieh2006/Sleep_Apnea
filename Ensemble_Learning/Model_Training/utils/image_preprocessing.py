# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:22:01 2019

@author: USER
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm



def my_preprocessing(dataset, outsize=512, crop=False, pre_type="ori"):
   
    data=[]
    
    for image in tqdm(dataset):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
        cond = np.argwhere(thresh == 255)
        x_min, x_max, y_min, y_max = cond[:,0].min(), cond[:,0].max(), cond[:,1].min(), cond[:,1].max()
        cut_img = image[x_min:x_max, y_min:y_max]
        
        
        if cut_img.shape[0]==cut_img.shape[1]:
            new_img = cv2.resize(cut_img, (1024, 1024))

        else:        
            h, w = cut_img.shape[0], cut_img.shape[1]
            delta = (w-h)//2
        
            if delta>=0:
                if (w-h)%2!=0:
                    refl_img = np.vstack([cut_img[0:delta][::-1], cut_img, cut_img[-delta-1:][::-1]])
                else:
                    refl_img = np.vstack([cut_img[0:delta][::-1], cut_img, cut_img[-delta:][::-1]])
        
            else :
                delta = (h-w)//2
                if (h-w)%2!=0:
                    refl_img = np.hstack([cut_img[:,0:delta][:,::-1], cut_img, cut_img[:,-delta-1:][:,::-1]])
                else:
                    refl_img = np.hstack([cut_img[:,0:delta][:,::-1], cut_img, cut_img[:,-delta:][:,::-1]])
                
                
        
            dim = refl_img.shape[0]
            half = int(dim/2)-1
        
            # crop out circle:
            circle_mask = np.zeros((dim, dim), np.uint8)
            circle_mask = cv2.circle(circle_mask, (half, half), half, 1, thickness=-1)
        
            print("refl_img.shape:" , refl_img.shape , "mask= ", circle_mask.shape)
            cir_img = cv2.bitwise_and(refl_img, refl_img, mask=circle_mask)
            cir_gray = cv2.cvtColor(cir_img, cv2.COLOR_BGR2GRAY)
            ret, thresh2 = cv2.threshold(cir_gray, 10,255, cv2.THRESH_BINARY)
        
            cond = np.argwhere(thresh2 > 0)
            x_min, x_max, y_min, y_max = cond[:,0].min(), cond[:,0].max(), cond[:,1].min(), cond[:,1].max()
            y_dis = (y_max-y_min)//2 
            x_cen = cir_img.shape[0]//2

            new_img = cir_img[x_cen-y_dis:x_cen+y_dis, y_min:y_max]
        
            new_img = cv2.resize(new_img, (1024, 1024))
             
         
        if crop:
            new_img = new_img[512-400:512+400, 512-400:512+400]
            new_img = cv2.resize(new_img, (outsize, outsize))
        else:
            new_img = cv2.resize(new_img, (outsize, outsize))
            
            
        if pre_type == "his":
            new_img = pre_his(new_img)
        elif pre_type == "cla":
            new_img = pre_cla(new_img)
        elif pre_type == "gau":
            new_img = pre_gau(new_img)
        else:
            new_img = new_img
            
            
        data.append(new_img) 
        
    return np.array(data)
 


def pre_his(cir_img):
    yuv = cv2.cvtColor(cir_img, cv2.COLOR_BGR2YUV)
    channels = cv2.split(yuv)
    channels[0] = cv2.equalizeHist(channels[0])
    yuv = cv2.merge(channels, yuv)
    his_img = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    return his_img


def pre_cla(cir_img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cla_img = np.zeros_like(cir_img)
    cla_img[:,:,0] = clahe.apply(cir_img[:,:,0])
    cla_img[:,:,1] = clahe.apply(cir_img[:,:,1])
    cla_img[:,:,2] = clahe.apply(cir_img[:,:,2])
    return cla_img

def pre_gau(cir_img):
    gau_img = cv2.addWeighted (cir_img, 4, cv2.GaussianBlur(cir_img , (0,0) , 30) ,-4 ,128)
    return gau_img
