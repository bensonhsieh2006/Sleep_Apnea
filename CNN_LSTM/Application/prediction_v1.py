import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from multiprocessing import Process
from memory_profiler import profile
import librosa
from librosa import display




def wav_to_mel(file, input_path, output_path):

    print(f'{file}: Converting...')
    fmax = 8192
    input_path = f'{input_path}\{file}.wav'
    output_path = f'{output_path}\{file}.png'
    

    y, sr = librosa.load(input_path)
    melspec = librosa.feature.melspectrogram(y,sr,
                                    n_mels=256,
                                    n_fft=8192,
                                    fmax=fmax)
    logmelspec = librosa.power_to_db(melspec)


    fig,ax = plt.subplots()
    img = display.specshow(logmelspec, cmap='magma', sr=sr,                         
                         fmax=fmax, ax=ax)
    cbar = fig.colorbar(img)
    cbar.mappable.set_clim(-40, 40)
    cbar.remove()


    plt.savefig(output_path)
    print(f'{file}: Mel Transfer Done.')
    
    return



def pre_his(img):

	yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

	y, u, v = cv2.split(yuv)
	y = cv2.equalizeHist(y)
	yuv = cv2.merge([y, u, v])

	yuv = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
	return yuv



def processing(file, mel_path):

    os.chdir(mel_path)
    img = cv2.imread(f'{file}.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    rect_mask = np.zeros(img.shape[:2], dtype="uint8")       	
    cv2.rectangle(rect_mask,(79,57),(576,427),255,-1)          	
    img = cv2.bitwise_and(img, img, mask=rect_mask)   

    img = img[57:427,79:576]
    img = cv2.resize(img, (448, 448))
    img = pre_his(img)
    img = cv2.normalize(img, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    del rect_mask
 	 
    return np.array(img)
    


def apnea_predict(count, mel_path, model_path):
    X_pred = []
    for x in range(count-10, count):
        X_pred.append(processing("segment"+str(x), mel_path))

    model = tf.keras.models.load_model(model_path)
    pred = model.predict(np.array([X_pred]))
    print(f'From {count-10} to {count-1} segment prediction: {pred}')

    return


def main(seg_path, mel_path, model_path):

    wav_list = []
    count_list = [0]
    count = 0

    while True:
        for file in os.listdir(seg_path):
            if file.endswith("wav") and file not in wav_list:
                wav_list.append(file)
                thread = Process(target=wav_to_mel, args=(file[:-4], seg_path, mel_path, ))
                thread.start()
                thread.join()
                count+=1
        
        if count%10==0 and count not in count_list:
            count_list.append(count)
            thread = Process(target=apnea_predict, args=(count, mel_path, model_path, ))
            thread.start()
            thread.join()


if __name__ == "__main__":

    seg_path = r'D:\Programs\Python\Project\Sleep_Apnea_App\LSTM\Segments'
    mel_path = r'D:\Programs\Python\Project\Sleep_Apnea_App\LSTM\Mel'
    model_path = r'D:\Programs\Python\Project\Sleep_Apnea_App\LSTM\Models\lstm_v1_30s_10_best.h5'
    

    main(seg_path, mel_path, model_path)