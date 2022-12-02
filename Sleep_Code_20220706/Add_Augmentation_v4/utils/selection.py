import os
import sys
from utils import implement_aug



def full_path(path, year=None, month=None, Date_and_ID=None):

    if Date_and_ID == None:

        if sys.platform == 'win32':
            fullpath = f'{path}\\{year}年\\{month}月'

        if sys.platform == 'linux':
            fullpath = f'{path}/{year}年/{month}月'


    elif year == None and month == None:

        if sys.platform == 'win32':
            fullpath = f'{path}\\{Date_and_ID[0:4]}\\{Date_and_ID[5:]}'

        if sys.platform == 'linux':
            fullpath = f'{path}/{Date_and_ID[0:4]}/{Date_and_ID[5:]}'


    else:

        if sys.platform == 'win32':
            fullpath = f'{path}\\{year}年\\{month}月\\{Date_and_ID[0:4]}\\{Date_and_ID[5:]}'

        if sys.platform == 'linux':
            fullpath = f'{path}/{year}年/{month}月/{Date_and_ID[0:4]}/{Date_and_ID[5:]}'
    

    return fullpath, len(fullpath)




def type_select(input_number):
    
    aug_dict = {0:'Add_Gaussian_Noise',1:'Add_Background_Noise',2:'Add_Short_Noises',
                3:'Band_Pass_Filter'  ,4:'High_Pass_Filter',    5:'Low_Pass_Filter',
                6:'Frequency_Mask',    7:'Time_Mask',  8:'Reverse',  9:'Shift'}
    
    return aug_dict[input_number]





def check_file(augmentation_type, new_path):

    data = True

    for file in os.listdir(new_path):
        if file.endswith('_' + augmentation_type.lower() + '.wav'):
            data = False

    return data




def get_aug(ori_path, new_path, bg_path, noise_path, input_number):

    if input_number== 0:
        implement_aug.Add_Gaussian_Noise(ori_path, new_path)


    elif input_number == 1:
        implement_aug.Add_Background_Noise(ori_path, new_path, bg_path)


    elif input_number == 2:
        implement_aug.Add_Short_Noises(ori_path, new_path, noise_path)


    elif input_number == 3:
        implement_aug.Band_Pass_Filter(ori_path, new_path)


    elif input_number == 4:
        implement_aug.High_Pass_Filter(ori_path, new_path)


    elif input_number == 5:
        implement_aug.Low_Pass_Filter(ori_path, new_path)


    elif input_number == 6:
        implement_aug.Frequency_Mask(ori_path, new_path)


    elif input_number == 7:
        implement_aug.Time_Mask(ori_path, new_path)


    elif input_number == 8:
        implement_aug.Reverse(ori_path, new_path)


    elif input_number == 9:
        implement_aug.Shift(ori_path, new_path)

    else:
        raise ValueError("Wrong value.")


    return 'Finished.'