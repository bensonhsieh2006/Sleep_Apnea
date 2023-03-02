from utils.Preprocessing import Preprocessing, Data_Augmentation

year = 2021
month = 9
proj_path = r'/NAS/Benson/Sleep_Apnea'
bg_path =  f'{proj_path}/Sleep_Codes/Sleep_Code_20221201/audiomentations/demo/background_noises'
noise_path = f'{proj_path}/Sleep_Codes/Sleep_Code_20221201/audiomentations/demo/short_noises'


folder_name = """
Select Folder:
0 : Wav_30_68
1 : Wav_Combine
2 : None
3 : Add_Gaussian_Noise
4 : Add_Background_Noise
5 : Add_Short_Noises
6 : Band_Pass_Filter
7 : High_Pass_Filter
8 : Low_Pass_Filter
9 : Frequency_Mask
10 : Time_Mask
11 : Reverse
12 : Shift
"""

type_dict = {
    0 : "Wav_30_68",
    1 : "Wav_Combine",
    2 : "None",
    3 : "Gau",
    4 : "Bac",
    5 : "Short",
    6 : "Band",
    7 : "High",
    8 : "Low",
    9 : "Freq",
    10 : "Time",
    11 : "Rev",
    12 : "Sft"
}

num = int(input("""
Select Step:
(1 month at once)
0 : Append_Directory
1 : Asf_to_Wav
2 : Wav_Combine
3 : Wav_to_Mel
4 : Wav_to_MFCC
5 : Add_Augmentation
Input:  """))

assert 0<=num<=5, "Step doesn't exist."
if num <= 4:

    preprocessing = Preprocessing(year, 
                                  month, 
                                  f'{proj_path}/Sleep_Code_Data/Temporary_Files',
                                  f'{proj_path}/Sleep_Code_Data/Raw Data')

    # create a csv file that contains:
    # 1. patient's examination date and ID    
    # 2. full path to raw data video.asf
    
    
    # preprocessing.patient_csv()

    preprocessing.read_patient_csv()
    if num == 0:

        imp_type = int(input(folder_name))
        assert 0<=imp_type<=12, "Folder doesn't exist."

        if imp_type >= 2:
            preprocessing.append_directory(f'{proj_path}/Sleep_Code_Data/Aug/Aug_{type_dict[imp_type]}')

        else:
            preprocessing.append_directory(f'{proj_path}/Sleep_Code_Data/{type_dict[imp_type]}')

    elif num == 1:
        preprocessing.asf_to_wav(f'{proj_path}/Sleep_Code_Data/Wav_30_68')

    elif num == 2:
        preprocessing.wav_combine(f'{proj_path}/Sleep_Code_Data/Wav_30_68', f'{proj_path}/Sleep_Code_Data/Wav_Combine')

    elif num == 3:

        imp_type = int(input(folder_name))
        assert 2<=imp_type<=12, "Selection doesn't exist."

        if imp_type == 2:
            preprocessing.wav_to_mel(f'{proj_path}/Sleep_Code_Data/Wav_Combine', f'{proj_path}/Sleep_Code_Data/Spectrograms/All_Mel_{type_dict[imp_type]}')
        
        else:
            preprocessing.wav_to_mel(f'{proj_path}/Sleep_Code_Data/Aug/Aug_{type_dict[imp_type]}', f'{proj_path}/Sleep_Code_Data/Spectrograms/All_Mel_{type_dict[imp_type]}')

    elif num == 4:

        imp_type = int(input(folder_name))
        assert 2<=imp_type<=12, "Selection doesn't exist."

        if imp_type == 2:
            preprocessing.wav_to_mfcc(f'{proj_path}/Sleep_Code_Data/Wav_Combine', f'{proj_path}/Sleep_Code_Data/Spectrograms/All_MFCC_{type_dict[imp_type]}')
        
        else:
            preprocessing.wav_to_mfcc(f'{proj_path}/Sleep_Code_Data/Aug/Aug_{type_dict[imp_type]}', f'{proj_path}/Sleep_Code_Data/Spectrograms/All_MFCC_{type_dict[imp_type]}')

else:

    add_aug = Data_Augmentation(year, 
                                month,
                                f'{proj_path}/Sleep_Code_Data/Temporary_Files',
                                f'{proj_path}/Sleep_Code_Data/Raw Data')
    
    # create a csv file that contains:
    # 1. patient's examination date and ID    
    # 2. full path to raw data video.asf
    
    # add_aug.patient_csv()

    add_aug.read_patient_csv()

    imp_num = int(input(folder_name))
    assert 3<=imp_num<=12, "Selection doesn't exist."

    add_aug.imp_aug(f'{proj_path}/Sleep_Code_Data/Wav_Combine',
                    f'{proj_path}/Sleep_Code_Data/Aug/Aug_{type_dict[imp_num]}',
                    imp_num,
                    bg_path,
                    noise_path)
