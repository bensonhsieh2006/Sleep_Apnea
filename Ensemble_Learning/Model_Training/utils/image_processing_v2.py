import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm

def my_processing(dataset, outsize, pre_type='his'):
    
    data = []
    
    for image in tqdm(dataset):                                        #image to crop

        rect_mask = np.zeros(image.shape[:2], dtype="uint8")           #black mask with shape of spectrogram 
        cv2.rectangle(rect_mask,(79,58),(478,427),255,-1)              #fill area that we want to keep with white

        masked_image = cv2.bitwise_and(image, image, mask=rect_mask)   #apply


        output_image = masked_image[58:427,80:478]                     #resize image to fit in model
        output_image = cv2.resize(output_image, (outsize,outsize))
        
        if pre_type == 'his':
            output_image = pre_his(output_image)
        
        data.append(output_image)
    
    return np.array(data)


def pre_his(cir_img):
    yuv = cv2.cvtColor(cir_img, cv2.COLOR_BGR2YUV)
    channels = cv2.split(yuv)
    channels[0] = cv2.equalizeHist(channels[0])
    yuv = cv2.merge(channels, yuv)
    his_img = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    return his_img