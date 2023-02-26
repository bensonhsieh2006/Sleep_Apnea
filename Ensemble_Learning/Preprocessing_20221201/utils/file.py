import sys
import os
import pandas as pd


def make_new_folder(name, parent_path):

    if name not in os.listdir(parent_path):
        os.mkdir(name)
        print(f'{name}: Added')

    else:
        print(f'{name}: Folder already exists.')



#Example:
#Input: C:\Users\user\Documents\Benson\Raw_Data, 2021, 1
#Output: C:\Users\user\Documents\Benson\Raw_Data\2021\1月, 47 
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



#Output: 0104 00000644-100839
def Date_and_ID(path, fullpath_len):

    Date_ID = path[fullpath_len+1:fullpath_len+5]+" "+path[-21:-6]

    return Date_ID



#create a csv file that contains patient's examination date and ID
def patient_info(csv_path, raw_path, raw_path_len, year, month):

    os.chdir(csv_path)
    Date_and_ID_list = []
    full_raw_path = []

    for root, directory, files in os.walk(raw_path):
        if root.endswith('Video'):
            Date_and_ID_list.append(Date_and_ID(root, raw_path_len))
            full_raw_path.append(root)


    Date_and_ID_list = sorted(Date_and_ID_list)
    new_full_raw_path = []
    for x in range(len(Date_and_ID_list)):
        for y in range(len(full_raw_path)):
            if Date_and_ID_list[x][5:] in full_raw_path[y]:
                new_full_raw_path.append(full_raw_path[y])
                

    df = pd.DataFrame(Date_and_ID_list)
    name = f'Date_and_ID_list_{year}_{month}.csv'
    df.to_csv(name, index=False)
    print(f'{name} :Done')

    df = pd.DataFrame(new_full_raw_path)
    name = f'Full_Raw_path_{year}_{month}.csv'
    df.to_csv(name, index=False)
    print(f'{name} :Done')