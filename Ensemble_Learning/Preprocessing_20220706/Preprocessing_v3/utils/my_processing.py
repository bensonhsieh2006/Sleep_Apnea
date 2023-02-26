from utils import file, audio_processing
import os
import pandas as pd
import sys
import time
import gc



class MyProcessing():

    def __init__(self,
                year,
                month,
                csv_path, 
                DateID_list = None,
                fulrwpath_list = None):
        
        self.year = year
        self.month = month
        self.csv_path = csv_path
        self.DateID_list = DateID_list
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


    def patient_csv(self, rw_path):

        raw_fullpath, raw_len_fullpath = file.full_path(rw_path, self.year, self.month)
        file.patient_info(self.csv_path, raw_fullpath, raw_len_fullpath, self.year, self.month)


    
    def read_patient_csv(self):

        os.chdir(self.csv_path)

        try:
            name = f'Date_and_ID_list_{self.year}_{self.month}.csv'
            self.DateID_list = (x for x in pd.read_csv(name)['0'])

            name = f'Full_Raw_path_{self.year}_{self.month}.csv'
            self.fulrwpath_list = (x for x in pd.read_csv(name)['0'])
            
        except FileNotFoundError:
            print(f'File: \'{name}\' not found')



    def append_directory(self, apd_path):

        self.require_warning(self.DateID_list, self.fulrwpath_list)

        #Append Directory

        os.chdir(apd_path)
        year_new_path = f'{self.year}年'
        month_new_path = f'{self.month}月'


        file.make_new_folder(year_new_path, os.getcwd())
        os.chdir(year_new_path)

        file.make_new_folder(month_new_path, os.getcwd())
        os.chdir(month_new_path)

        date = sorted(set(x[0:4] for x in self.DateID_list))
        for x in date:
            file.make_new_folder(x[0:4], os.getcwd())


        #Append SubDirectory
        self.read_patient_csv()
        for x in self.DateID_list:

            
            if sys.platform == 'win32':
                fullpath = f'{file.full_path(apd_path, self.year, self.month)[0]}\\{x[0:4]}'

            if sys.platform == 'linux':
                fullpath = f'{file.full_path(apd_path, self.year, self.month)[0]}/{x[0:4]}'
                

            os.chdir(fullpath)
            print(fullpath)

            file.make_new_folder(x[5:], os.getcwd())

        

    

    def asf_to_wav(self, extwav_path):

        self.require_warning(self.DateID_list, self.fulrwpath_list)

        #Extract
        num_list = [x for x in range(30,69)]
        for x,y in zip(self.DateID_list, self.fulrwpath_list):


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

        self.require_warning(self.DateID_list, self.fulrwpath_list)

        #Combine
        num_list = [x for x in range(30,69)]
        for x in self.DateID_list:

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

        self.require_warning(self.DateID_list, self.fulrwpath_list)
        stop_iter = False
        count = 0 

        for x in self.DateID_list:

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
                        # count+=1
                        # if count>=10:
                        #     stop_iter = True
                        break

                    else:
                        print(f'{files}: Already transferred')
            # if stop_iter:
            #     break
            


    
    
    def wav_to_mfcc(self, trans_path, mfcc_path):
        
        self.require_warning(self.DateID_list, self.fulrwpath_list)
        stop_iter = False
        count=0
        for x in self.DateID_list:

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
                        # count+=1
                        # if count>=20:
                        #     stop_iter = True
                        break

                    else:
                        print(f'{files}: Already transferred')
            
            # if stop_iter:
            #     break