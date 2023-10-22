import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from multiprocessing import Process, Queue
import librosa
from librosa import display
import tkinter as tk
from PIL import ImageTk, Image
import time

from plot import plot_overall_img

class App():

    def __init__(self, q, total_seg):

        self.q = q
        self.total_seg = total_seg

        self.win = tk.Tk()
        self.win.geometry('600x500')
        self.win.title("Sleep Apnea")
        self.win.resizable(False,False)

        self.frame = tk.Frame(self.win)
        self.frame.pack(side="top", expand=True, fill="both")
        
        self.initialize()
        self.running()
        self.win.after(1000, self.update)
        self.win.mainloop()


    def update(self):
        
        if not self.q.empty():
            
            self.count+=1
            self.label_list.append(self.q.get_nowait()) 
            print(self.label_list[-1])

            # if len(self.label_list)>3:
            #     self.label_list.pop(0)


            if self.label_list[-1][1] == 0:
                self.cur_result['text'] = None
                self.cur_result['image'] = self.green_img
            
            else:
                self.cur_result['text'] = None
                self.cur_result['image'] = self.red_img


            if len(self.label_list) > 0:
                # print(self.label_list[-1][0])

                if self.label_list[-1][1] == 0:
                    self.mel23['image'] = self.green_img
                else:
                    self.mel23['image'] = self.red_img
                    
                self.mel3_lk = Image.open(f'.\Mel\segment{self.label_list[-1][0]}.png')
                self.mel3_lk = self.mel3_lk.resize((130,130), Image.ANTIALIAS)
                self.mel3 = ImageTk.PhotoImage(self.mel3_lk)
                self.mel33['image'] = self.mel3

            if len(self.label_list) > 1:
                # print(self.label_list[-2][0])

                if self.label_list[-2][1] == 0:
                    self.mel22['image'] = self.green_img
                else:
                    self.mel22['image'] = self.red_img

                self.mel2_lk = Image.open(f'.\Mel\segment{self.label_list[-2][0]}.png')
                self.mel2_lk = self.mel2_lk.resize((130,130), Image.ANTIALIAS)
                self.mel2 = ImageTk.PhotoImage(self.mel2_lk)
                self.mel32['image'] = self.mel2

            if len(self.label_list) > 2:
                # print(self.label_list[-3][0])

                if self.label_list[-3][1] == 0:
                    self.mel21['image'] = self.green_img
                else:
                    self.mel21['image'] = self.red_img

                self.mel1_lk = Image.open(f'.\Mel\segment{self.label_list[-3][0]}.png')
                self.mel1_lk = self.mel1_lk.resize((130,130), Image.ANTIALIAS)
                self.mel1 = ImageTk.PhotoImage(self.mel1_lk)
                self.mel31['image'] = self.mel1

            print(self.count)
            if self.count == self.total_seg-9:
                time.sleep(5)
                plot_overall_img(self.label_list)

        self.win.after(1000, self.update)

    def running(self):

        self.title = tk.Label(self.frame, text='Sleep Apnea Continuous Detection', font=self.font_1, fg='blue')
        self.title.place(x=35, y=50)

        self.word = tk.Label(self.frame, text='Predicting... ', font=self.font_2, fg='blue')
        self.word.place(x=35, y=120)

        self.des1 = tk.Label(self.frame, text='(Negative:          Positive:     )', font=self.font_3)
        self.des1.place(x=200, y=125)

        self.green_icon = tk.Label(self.frame, image=self.green_img)
        self.green_icon.place(x=300, y=120)

        self.red_icon = tk.Label(self.frame, image=self.red_img)
        self.red_icon.place(x=450, y=120)

        self.des2 = tk.Label(self.frame, text='Current Result: ', font=self.font_3, fg='black')
        self.des2.place(x=35, y=200)

        self.cur_result = tk.Label(self.frame, text='Waiting...', font=self.font_3, fg='black')
        self.cur_result.place(x=200, y=195)

        self.timeline = tk.Label(self.frame, text='———————————————————————> Time', font=self.font_3, fg='black')
        self.timeline.place(x=30, y=240)

        self.mel11 = tk.Label(self.frame, text='Past 90s', font=self.font_3, fg='black', borderwidth=2, relief='solid')
        self.mel11.place(x=30, y=270, width=179, height=29)

        self.mel12 = tk.Label(self.frame, text='Past 60s', font=self.font_3, fg='black', borderwidth=2, relief='solid')
        self.mel12.place(x=210, y=270, width=179, height=29)

        self.mel13 = tk.Label(self.frame, text='Past 30s', font=self.font_3, fg='black', borderwidth=2, relief='solid')
        self.mel13.place(x=390, y=270, width=179, height=29)

        self.mel21 = tk.Label(self.frame, fg='black', borderwidth=2, relief='solid')
        self.mel21.place(x=30, y=300, width=179, height=49)

        self.mel22 = tk.Label(self.frame, fg='black', borderwidth=2, relief='solid')
        self.mel22.place(x=210, y=300, width=179, height=49)

        self.mel23 = tk.Label(self.frame, fg='black', borderwidth=2, relief='solid')
        self.mel23.place(x=390, y=300, width=179, height=49)

        self.mel31 = tk.Label(self.frame, fg='black', borderwidth=2, relief='solid')
        self.mel31.place(x=30, y=350, width=179, height=145)

        self.mel32 = tk.Label(self.frame, fg='black', borderwidth=2, relief='solid')
        self.mel32.place(x=210, y=350, width=179, height=145)

        self.mel33 = tk.Label(self.frame, fg='black', borderwidth=2, relief='solid')
        self.mel33.place(x=390, y=350, width=179, height=145)

    def initialize(self):

        self.label_list = []
        self.count = 0

        self.font_1 = 'Arial 26'
        self.font_2 = 'Arial 20'
        self.font_3 = 'Arial 16'

        self.red_img_lk = Image.open("red_light.png")
        self.red_img_lk = self.red_img_lk.resize((40,40), Image.ANTIALIAS)
        self.red_img = ImageTk.PhotoImage(self.red_img_lk)

        self.green_img_lk = Image.open("green_light.png")
        self.green_img_lk = self.green_img_lk.resize((40,40), Image.ANTIALIAS)
        self.green_img = ImageTk.PhotoImage(self.green_img_lk)


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
    


def apnea_predict(count, mel_path, model_path, q):
    X_pred = []
    for x in range(count-10, count):
        X_pred.append(processing(f'segment{str(x)}', mel_path))

    model = tf.keras.models.load_model(model_path)
    pred = model.predict(np.array([X_pred]))
    pred = np.around(pred, decimals=3)
    print(f'From {count-10} to {count-1} segment prediction: {pred}')
    q.put([count-1, pred.argmax(-1)], block=False)
    return


def predict(seg_path, mel_path, model_path, q):

    wav_list = []
    count_list = []
    count = 0
    while True:
        for file in os.listdir(seg_path):
            if file.endswith("wav") and file not in wav_list:
                wav_list.append(file)
                thread = Process(target=wav_to_mel, args=(file[:-4], seg_path, mel_path, ))
                thread.start()
                thread.join()
                count+=1
        
        if count>=10 and count not in count_list:
            count_list.append(count)
            thread = Process(target=apnea_predict, args=(count, mel_path, model_path, q, ))
            thread.start()
            thread.join()


def run_app(q, total_seg):
    app = App(q, total_seg)

if __name__ == "__main__":

    seg_path = r'C:\Users\user\Desktop\Application\Segments'
    mel_path = r'C:\Users\user\Desktop\Application\Mel'
    model_path = r'D:\Programs\Python\Project\Sleep_Apnea_App\LSTM\Models\lstm.h5'
    q = Queue()

    thread1 = Process(target=predict, args=(seg_path, mel_path, model_path, q, ))
    thread1.start()

    thread2 = Process(target=run_app, args=(q, 30, ))
    thread2.start()
    
    # for x in range(21):
    #     if x == 2 or x == 8 or x == 20:
    #         q.put([x, 1])
    #     else:
    #         q.put([x, 0])
    #     time.sleep(2)