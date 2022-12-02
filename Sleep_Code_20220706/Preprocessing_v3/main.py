from utils import my_processing,file
import time

def main():
    #Last Modified: 20220709
    ################# parameters ###################################

    year = 2021
    month = 9
    

    csv_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Temporary_Files'
    rw_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Raw Data'
    extwav_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Wav_30_68'
    combwav_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Wav_Combine'

    apd_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Aug/Aug_Gau'
    trans_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Aug/Aug_Gau'
    mel_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Spectrograms/All_Mel_Gau'
    mfcc_path = r'/NAS/Benson/Sleep_Apnea/Sleep_Code_Data/Spectrograms/All_MFCC_Gau'

    ################# parameters ###################################






    preprocess = my_processing.MyProcessing(year=year, 
                                            month=month, 
                                            csv_path=csv_path,
                                            )

    # create a csv file that contains:
    # 1. patient's examination date and ID    
    # 2. full path to raw data video.asf
    
    # preprocess.patient_csv(rw_path)


    preprocess.read_patient_csv()


    num = int(input('''
    Please select Step:
    (1 file at once)
    0 : Append_Directory
    1 : Asf_to_Wav
    2 : Wav_Combine
    3 : Wav_to_Mel
    4 : Wav_to_MFCC
    Input: 
    '''))

    assert 0<=num<=4, 'Input must be an integer from 0 to 4'
    start_time = time.perf_counter()
    if num==0:
        preprocess.append_directory(apd_path)
    elif num==1:
        preprocess.asf_to_wav(extwav_path)
    elif num==2:
        preprocess.wav_combine(extwav_path, combwav_path)
    elif num==3:
        preprocess.wav_to_mel(trans_path, mel_path)
    elif num==4:
        preprocess.wav_to_mfcc(trans_path, mfcc_path)
    end_time = time.perf_counter()
    print(f'Time: {end_time-start_time} sec')

if __name__=='__main__':
    main()


    
