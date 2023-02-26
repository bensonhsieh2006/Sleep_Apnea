from utils import file
import os
import pandas as pd
import sys


################# parameters ###################################


#csv_file path
csv_path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Temporary_Files'

#Raw_Data path
path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Raw Data'    
year = 2021
month = 3

#Wav_Combine path
#new_path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Wav_Combine'

#All_Mel path
#new_path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/All_MFCC'  

#new_path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Wav_30_68'

new_path = r'/home/why/Projects/Sleep_Apnea/Sleep_Code_Data/Aug/Aug_Gaussian'


################# parameters ###################################





# create a csv file that contains:
# 1. patient's examination date and ID    
# 2. full path to raw data video.asf
#'''
 
# raw_fullpath, raw_len_fullpath = file.full_path(path, year, month)
# file.patient_info(csv_path, raw_fullpath, raw_len_fullpath, year, month)

#'''


#'''

#read csv file
os.chdir(csv_path)
Date_and_ID = pd.read_csv(f'Date_and_ID_list_{year}_{month}.csv')
Date_and_ID_list = (x for x in Date_and_ID['0'])

#'''

# '''   Append Directory

os.chdir(new_path)
year_new_path = f'{year}年'
month_new_path = f'{month}月'


file.make_new_folder(year_new_path, os.getcwd())
os.chdir(year_new_path)

file.make_new_folder(month_new_path, os.getcwd())
os.chdir(month_new_path)

date = sorted(set(x[0:4] for x in Date_and_ID_list))
for x in date:
    file.make_new_folder(x[0:4], os.getcwd())

#'''


#'''   Append SubDirectory

for x in Date_and_ID_list:

    if sys.platform == 'win32':
        fullpath = f'{file.full_path(new_path, year, month)[0]}\\{x[0:4]}'

    if sys.platform == 'linux':
        fullpath = f'{file.full_path(new_path, year, month)[0]}/{x[0:4]}'

    os.chdir(fullpath)
    print(fullpath)

    file.make_new_folder(x[5:], os.getcwd())

#'''

