from utils import file, audio_processing
import pandas as pd
import os
import sys


################# parameters ###################################

csv_path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Temporary_Files'

path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Raw_Data'   #Raw_Data path
year = 2021
month = 2

new_path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Wav_30_68'     #Wav_Combine path


################# parameters ###################################

os.chdir(csv_path)
name = f'Date_and_ID_list_{year}_{month}.csv'
Date_and_ID_list = pd.read_csv(name)
Date_and_ID_list = [x for x in Date_and_ID_list['0']]

name = f'Full_Raw_path_{year}_{month}.csv'
full_raw_path = pd.read_csv(name)
full_raw_path = [x for x in full_raw_path['0']]


count = 0
#Extract
num_list = [x for x in range(30,69)]
for x in range(len(Date_and_ID_list)):

    if count!=1:

        data=True
        source_list=[]
        raw_path = full_raw_path[x]
        dest_path = file.full_path(new_path, year, month, Date_and_ID_list[x])[0]
        os.chdir(raw_path)

        for files in os.listdir(dest_path):

            if files.endswith('.wav'):
                data = False

        if data:
            #'''
            for y in num_list:

                if sys.platform == 'win32':
                    source_list.append(f'{raw_path}\\{files}')
                    print((f'{raw_path}\\00{num_list}.asf'))

                if sys.platform == 'linux':
                    full_path = f'{raw_path}/00{y}.asf'
                    dst_path = f'{dest_path}/00{y}.wav'
                    
                    audio_processing.transfer(full_path, dst_path)
            count+=1
            #'''