import pandas as pd
import os



def check(spec_type, aug_type):

    path =r'/home/why/Projects/Sleep_Apnea/Deep_Learning/sleep_data_v2/Spectrograms/All_'+spec_type+'_'+aug_type
    print(f'spec_type: {spec_type}, aug_type:{aug_type}')

    id_list=sorted([file[:-4] for file in os.listdir(path)])
    print(len(id_list))


    name_ids = [x for x in pd.read_csv('name.csv')['Number']]
    print(len(name_ids))

    #check if (id.png) is in (name.csv)
    count=0
    for id in id_list:

        if id not in name_ids:

            print(f'{id}: False')
            count+=1

    print(f'False count: {count}')
    print()

    # count=0
    # for id in name_ids:

    #     if id not in id_list:

    #         print(f'{id}: False')
    #         count+=1

    # print(f'False count: {count}')

spec_type = ['Mel', 'MFCC']
aug_type = ['None', 'Gau', 'Bac', 'Short', 'Band', 'High', 'Low', 'Freq', 'Time', 'Rev', 'Sft']

if __name__ == '__main__':
    for x in spec_type:
        for y in aug_type:
            check(x, y)