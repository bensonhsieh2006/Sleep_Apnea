import pandas as pd
import os
import shutil




def add(spec_type, aug_type):

    path =r'/home/why/Projects/Sleep_Apnea/Deep_Learning/sleep_data_v2/Spectrograms/All_' + spec_type + '_' + aug_type
    data_path = r'/home/why/Projects/Sleep_Apnea/Deep_Learning/sleep_data_v2/Training_Data'
    train_name = spec_type + '_Train_' + aug_type
    test_name = spec_type + '_Test_' + aug_type
    train_path = os.path.join(data_path, train_name)
    test_path = os.path.join(data_path, test_name)
    print(f'spec_type: {spec_type}, aug_type:{aug_type}')

    if train_name not in os.listdir(data_path):
        os.mkdir(train_path)

    if test_name not in os.listdir(data_path):
        os.mkdir(test_path)


    train_ids = [x for x in pd.read_csv('train.csv')['Number']]
    print(len(train_ids))


    test_ids = [x for x in pd.read_csv('test.csv')['Number']]
    print(len(test_ids))

    id_list=sorted([file[:-4] for file in os.listdir(path)])
    print(len(id_list))



    #copy each (id.png) in (All_Mel/All_MFCC) to (Mel_train/MFCC_train) that is listed in (train.csv)
    count=0
    for id in train_ids:

        if id in id_list:

            src = f'{path}/{id}.png'
            dst = f'{train_path}/{id}.png'

            if f'{id}.png' not in os.listdir(train_path):
                shutil.copyfile(src, dst)

        else:
            print(f'{id}: False')
            count+=1

    print(f'Train false count: {count}')



    #copy each (id.png) in (All_Mel/All_MFCC) to (Mel_test/MFCC_test) that is listed in (test.csv)
    count=0
    for id in test_ids:

        if id in id_list:

            src = f'{path}/{id}.png'
            dst = f'{test_path}/{id}.png'

            if f'{id}.png' not in os.listdir(test_path):
                shutil.copyfile(src, dst)

        else:
            print(f'{id}: False')
            count+=1
            
    print(f'Test false count: {count}')


spec_type = ['Mel', 'MFCC']
aug_type = ['None', 'Gau', 'Bac', 'Short', 'Band', 'High', 'Low', 'Freq', 'Time', 'Rev', 'Sft']

if __name__ == '__main__':
    for x in spec_type:
        for y in aug_type:
            add(x, y)