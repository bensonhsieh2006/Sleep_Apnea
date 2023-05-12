from utils import file, audio_processing, implement_aug
import os
import sys
import pandas as pd




class Basic_Preprocessing():

    def __init__(self, 
                 year, 
                 month, 
                 csv_path, 
                 rw_path, 
                 Date_ID_list = None, 
                 fulrwpath_list = None):
        
        self.year = year
        self.month = month
        self.csv_path = csv_path
        self.rw_path = rw_path
        self.Date_ID_list = Date_ID_list
        self.fulrwpath_list = fulrwpath_list



    def require_warning(self, DateID_list, fulrwpath_list):

        assert DateID_list!=None, 'Date_and_ID_list required'
        assert fulrwpath_list!=None, 'full_raw_path_list required'



    def check_file(self, tar_path, tar_file):

        bool = True

        for file in os.listdir(tar_path):
            if file.endswith(tar_file):
                bool = False
        
        return bool



    def patient_csv(self):

        raw_fullpath, raw_len_fullpath = file.full_path(self.rw_path, self.year, self.month)
        file.patient_info(self.csv_path, raw_fullpath, raw_len_fullpath, self.year, self.month)


    
    def read_patient_csv(self):

        os.chdir(self.csv_path)

        try:
            name = f'Date_and_ID_list_{self.year}_{self.month}.csv'
            self.Date_ID_list = (x for x in pd.read_csv(name)['0'])

            name = f'Full_Raw_path_{self.year}_{self.month}.csv'
            self.fulrwpath_list = (x for x in pd.read_csv(name)['0'])
            
        except FileNotFoundError:
            print(f'File: \'{name}\' not found')



class Preprocessing(Basic_Preprocessing):


    def __init__(self, year, month, csv_path, rw_path, Date_ID_list = None, fulrwpath_list = None):
        super().__init__(year, month, csv_path, rw_path, Date_ID_list, fulrwpath_list)

    
    def append_directory(self, apd_path):


        self.require_warning(self.Date_ID_list, self.fulrwpath_list)

        #Append Directory

        os.chdir(apd_path)
        year_new_path = f'{self.year}年'
        month_new_path = f'{self.month}月'


        file.make_new_folder(year_new_path, os.getcwd())
        os.chdir(year_new_path)

        file.make_new_folder(month_new_path, os.getcwd())
        os.chdir(month_new_path)

        date = sorted(set(x[0:4] for x in self.Date_ID_list))
        for x in date:
            file.make_new_folder(x[0:4], os.getcwd())


        #Append SubDirectory
        self.read_patient_csv()
        for x in self.Date_ID_list:

            
            if sys.platform == 'win32':
                fullpath = f'{file.full_path(apd_path, self.year, self.month)[0]}\\{x[0:4]}'

            if sys.platform == 'linux':
                fullpath = f'{file.full_path(apd_path, self.year, self.month)[0]}/{x[0:4]}'
                

            os.chdir(fullpath)
            print(fullpath)

            file.make_new_folder(x[5:], os.getcwd())

        

    def asf_to_wav(self, extwav_path):

        self.require_warning(self.Date_ID_list, self.fulrwpath_list)

        #Extract
        num_list = [x for x in range(30,69)]
        for x,y in zip(self.Date_ID_list, self.fulrwpath_list):


            dest_path = file.full_path(extwav_path, self.year, self.month, x)[0]
            os.chdir(y)

            if self.check_file(dest_path, 'wav'):
                #'''
                for num in num_list:

                    if sys.platform == 'win32':

                        src_path = f'{y}\\00{num}.asf'
                        dst_path = f'{dest_path}\\00{num}.wav'
                        

                    if sys.platform == 'linux':
                        src_path = f'{y}/00{num}.asf'
                        dst_path = f'{dest_path}/00{num}.wav'
                        
                    audio_processing.transfer(src_path, dst_path)
                    #'''

    

    def wav_combine(self, extwav_path, combwav_path):

        self.require_warning(self.Date_ID_list, self.fulrwpath_list)

        #Combine
        num_list = [x for x in range(30,69)]
        for x in self.Date_ID_list:

            source_list=[]
            src_path = file.full_path(extwav_path, self.year, self.month, x)[0]
            dest_path = file.full_path(combwav_path, self.year, self.month, x)[0]
            os.chdir(src_path)

            if self.check_file(dest_path, 'wav'):
                #'''
                for num in num_list:

                    if sys.platform == 'win32':
                        full_path = f'{src_path}\\00{num}.wav'
                        source_list.append(full_path)

                    if sys.platform == 'linux':
                        full_path = f'{src_path}/00{num}.wav'
                        source_list.append(full_path)
                
                print(src_path)
                print(dest_path)
                audio_processing.CombineWav(source_list, dest_path)
                #'''

    

    def wav_to_mel(self, trans_path, mel_path):

        self.require_warning(self.Date_ID_list, self.fulrwpath_list)

        for x in self.Date_ID_list:

            source_path = file.full_path(trans_path, self.year, self.month, x)[0]
            os.chdir(source_path)
            for files in os.listdir():
                # Check whether file is in wav or not
                if files.endswith(".wav"):

                    if self.check_file(mel_path,f'{x[5:]}.png'):

                        source = f'{source_path}/{files}'
                        destination = f'{mel_path}/{x[5:]}.png'
                        print(source)
                        print(destination)

                        audio_processing.mel(source[:-4], destination[:-4])
                        break

                    else:
                        print(f'{files}: Already transferred')

            

    
    def wav_to_mfcc(self, trans_path, mfcc_path):
        
        self.require_warning(self.Date_ID_list, self.fulrwpath_list)

        for x in self.Date_ID_list:

            source_path = file.full_path(trans_path, self.year, self.month, x)[0]
            os.chdir(source_path)

            for files in os.listdir():

                # Check whether file is in wav or not
                if files.endswith(".wav"):

                    if self.check_file(mfcc_path, f'{x[5:]}.png'):

                        source = f'{source_path}/{files}'
                        destination = f'{mfcc_path}/{x[5:]}.png'
                        print(source)
                        print(destination)

                        audio_processing.mfcc(source[:-4], destination[:-4])
                        break

                    else:
                        print(f'{files}: Already transferred')



class Data_Augmentation(Basic_Preprocessing):


    def __init__(self, year, month, csv_path, rw_path, Date_ID_list = None, fulrwpath_list = None):
        super().__init__(year, month, csv_path, rw_path, Date_ID_list, fulrwpath_list)



    def type_select(self, i_num):
    
        aug_dict = {3:'Add_Gaussian_Noise',4:'Add_Background_Noise',5:'Add_Short_Noises',
                    6:'Band_Pass_Filter'  ,7:'High_Pass_Filter',    8:'Low_Pass_Filter',
                    9:'Frequency_Mask',    10:'Time_Mask',  11:'Reverse',  12:'Shift'}
    
        return aug_dict[i_num]



    def _get_aug(self, ori_path, new_path, bg_path, noise_path, i_num):

        if i_num == 3:
            implement_aug.Add_Gaussian_Noise(ori_path, new_path)


        elif i_num == 4:
            implement_aug.Add_Background_Noise(ori_path, new_path, bg_path)


        elif i_num == 5:
            implement_aug.Add_Short_Noises(ori_path, new_path, noise_path)


        elif i_num == 6:
            implement_aug.Band_Pass_Filter(ori_path, new_path)


        elif i_num == 7:
            implement_aug.High_Pass_Filter(ori_path, new_path)


        elif i_num == 8:
            implement_aug.Low_Pass_Filter(ori_path, new_path)


        elif i_num == 9:
            implement_aug.Frequency_Mask(ori_path, new_path)


        elif i_num == 10:
            implement_aug.Time_Mask(ori_path, new_path)


        elif i_num == 11:
            implement_aug.Reverse(ori_path, new_path)


        elif i_num == 12:
            implement_aug.Shift(ori_path, new_path)

        else:
            raise ValueError("Wrong value.")


        return 'Finished.'



    def imp_aug(self, ori_path, new_path, i_num, bg_path, noise_path):

        self.require_warning(self.Date_ID_list, self.fulrwpath_list)
        print(f'Augmentation: {self.type_select(i_num)}')

        for x in self.Date_ID_list:

            source_path = f'{file.full_path(ori_path, self.year, self.month, x)[0]}'
            dest_path = f'{file.full_path(new_path, self.year, self.month, x)[0]}'
            os.chdir(source_path)


            for files in os.listdir():
                # Check whether file is in wav or not
                if files.endswith("combined.wav"):

                    if self.check_file(dest_path, '_' + self.type_select(i_num).lower() + '.wav'):
                        source = f'{source_path}/{files}'
                        destination = f'{dest_path}/{files}'
                        print(source)
                        print(destination)

                        result = self._get_aug(source[:-4], destination[:-4], bg_path, noise_path, i_num)
                        print(result)

                    else:
                        print('Skipping...')