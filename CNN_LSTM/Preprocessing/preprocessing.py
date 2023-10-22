import librosa
from librosa import display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import moviepy.editor as mp
import os
from utils import file, audio_processing


seg_dur = 30
year = 2021
month = 5
num_list = [x for x in range(30,69)]
csv_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Temporary_Files' 
wav_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Wav_30_68'
seg_path = f'/NAS/Benson/Sleep_Apnea/Sleep_Codes/Github/Sleep_Apnea/CNN_LSTM/Model_Training/Data/Segments_{seg_dur}s'




name = f'{csv_path}/Date_and_ID_list_{year}_{month}.csv'
DateID_list = [x for x in pd.read_csv(name)['0']]

"""
Divides selected patient's audio(30~68th .asf file) 
to 30s audio per .wav file and converts them to mel spectrogram.)
"""
for x in [DateID_list[5]]:

    wave_path = file.full_path(wav_path, year, month, x)[0]
    print(wave_path)

    for num in num_list:

        full_wav_file = f'{wave_path}/00{num}.wav'

        y, sr = librosa.load(full_wav_file)
        fr_per_seg = seg_dur*22050

        for z in range(300//seg_dur):

            if (z+1)*fr_per_seg>=len(y):
                audio_processing.mel(f'{seg_path}/{x[5:]}_00{num}_{str(z)}', y[z*fr_per_seg:], sr)
            else:
                audio_processing.mel(f'{seg_path}/{x[5:]}_00{num}_{str(z)}', y[z*fr_per_seg:(z+1)*fr_per_seg], sr)

  


