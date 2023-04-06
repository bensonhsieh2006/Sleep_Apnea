import numpy as np
import cv2
from tqdm import tqdm

def my_processing(dataset, outsize, pre_type='his'):
    
    data = []
    
    for img in tqdm(dataset):                                        #image to crop

        rect_mask = np.zeros(img.shape[:2], dtype="uint8")           #black mask with shape of spectrogram 
        cv2.rectangle(rect_mask,(79,57),(576,427),255,-1)              #fill area we want to keep with white

        masked_img = cv2.bitwise_and(img, img, mask=rect_mask)   #apply


        output_img = masked_img[57:427,79:576]                    #resize image to fit in model
        output_img = cv2.resize(output_img, (outsize,outsize))

        if pre_type == 'his':
            output_img = pre_his(output_img)

        output_img = cv2.normalize(output_img, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        data.append(output_img)
    
    return np.array(data)


def pre_his(img):
    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(yuv)
    y = cv2.equalizeHist(y)
    yuv = cv2.merge([y, u, v])
    his_img = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
    return his_img