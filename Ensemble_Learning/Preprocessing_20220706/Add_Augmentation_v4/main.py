from utils import selection
import pandas as pd
import os
import time


ori_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Wav_Combine'
new_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Aug/Aug_Gau'
csv_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Temporary_Files'
year = 2021
month = 9


#Add_Background_Noise
bg_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Codes/Sleep_Code_20220706/Add_Augmentation_v4/audiomentations/demo/background_noises'

#Add_Short_Noises
noise_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Codes/Sleep_Code_20220706/Add_Augmentation_v4/audiomentations/demo/short_noises'


os.chdir(csv_path)
name = f'Date_and_ID_list_{year}_{month}.csv'
Date_and_ID_list = (x for x in pd.read_csv(name)['0'])



input_number = int(input('''
Please select augmentation:
(1 combined_wav is going to be implemented if haven't before)
0 : Add_Gaussian_Noise
1 : Add_Background_Noise
2 : Add_Short_Noises
3 : Band_Pass_Filter
4 : High_Pass_Filter
5 : Low_Pass_Filter
6 : Frequency_Mask
7 : Time_Mask
8 : Reverse
9 : Shift
Input: 
'''))

augmentation_type = selection.type_select(int(input_number))
print(augmentation_type)


start_time = time.perf_counter()
count=0
for x in Date_and_ID_list:

    if count!=40:

        source_path = f'{selection.full_path(ori_path, year, month, x)[0]}'
        dest_path = f'{selection.full_path(new_path, year, month, x)[0]}'
        os.chdir(source_path)


        for files in os.listdir():
            # Check whether file is in wav or not
            print(files)
            if files.endswith("combined.wav"):

                if selection.check_file(augmentation_type, dest_path):
                    source = f'{source_path}/{files}'
                    destination = f'{dest_path}/{files}'
                    print(source)
                    print(destination)

                    result = selection.get_aug(source[:-4], destination[:-4], bg_path, noise_path, input_number)
                    print(result)
                    # count+=1

                else:
                    print('Skipping...')
end_time = time.perf_counter()
print(f'Time: {end_time-start_time} sec')



    



