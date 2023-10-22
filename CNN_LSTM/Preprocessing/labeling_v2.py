import pandas as pd
import os



###Time calculating algorithms

#下午11:42:34 --> 23:42:34
def twenty_four_hr_clock(time):

    if time[:2] == "下午":
        return str(int(time[3:5]) + 12) + time[5:]
    elif time[3:5] == "12":
        return str(int(time[3:5]) - 12) + '0' + time[5:]
    else:
        return time[3:]



# adds a time with given seconds
def time_add(t1, sec):
    hr1, min1, sec1 = int(t1[:2]), int(t1[3:5]), float(t1[6:])

    time_sec = float((sec1 + sec) % 60)
    time_min = int((min1 + (sec1 + sec) // 60) % 60)
    time_hr = int((hr1 + (min1 + (sec1 + sec) // 60) // 60) % 12)
    time = f'{time_hr}:{time_min}:{time_sec}'

    if time_hr < 10:
        time = f'0{time}'
    if time_min<10:
        time = f'{time[:3]}0{time[3:]}'
    if time_sec<10:
        time = f'{time[:6]}0{time[6:]}'

    return time



#outputs (t2-t1) in seconds
def cal_duration(t1, t2):
    hr1, min1, sec1 = int(t1[:2]), int(t1[3:5]), float(t1[6:])
    hr2, min2, sec2 = int(t2[:2]), int(t2[3:5]), float(t2[6:]) 

    time_sec = (sec2 - sec1 + 60) % 60
    time_min = (min2 - min1 - (sec1 > sec2) + 60) % 60
    time_hr = (hr2 - hr1 - (min1 > min2 - (sec1 > sec2)) + 24) % 24

    return time_hr * 3600 + time_min * 60 + time_sec 




###Labeling algorithms

#calculate time proportion for each epoch of each event(mixed up)
def proportion(start_rec, event_list, label_list, sample, seg_time):
    # print()
    total_epoch = 11700//seg_time

    for time, duration in zip(event_list['Time'], event_list['Duration']):

        start_time = twenty_four_hr_clock(time)
        start_epoch = cal_duration(start_rec, start_time) / seg_time
        end_epoch = cal_duration(start_rec, time_add(start_time, duration)) / seg_time
        # print(start_epoch)
        if int(end_epoch) == int(start_epoch) and end_epoch <= total_epoch-1:
            label_list[int(end_epoch) + sample * total_epoch] += end_epoch - start_epoch

        else:
            for epoch in range(int(start_epoch), int(end_epoch) + 1):
                
                if epoch <= total_epoch-1:
                    if epoch < start_epoch:
                        label_list[epoch + sample * total_epoch] += epoch + 1 - start_epoch
                    elif end_epoch-epoch<1:
                        label_list[epoch + sample * total_epoch] += end_epoch - epoch
                    else:
                        label_list[epoch + sample * total_epoch] += 1

    return label_list



#calculate time proportion for each epoch of each event(class: [Hypopnea, Obstructive Apnea, Central Apnea, Mixed Apnea])
def multi_class_proportion(start_rec, event_list, label_list, sample, seg_time):

    event_dict = {'Hypopnea':0, 'Obstructive Apnea':1, 'Central Apnea':2, 'Mixed Apnea':3}
    total_epoch = 11700//seg_time

    for time, duration, event in zip(event_list['Time'], event_list['Duration'], event_list['Type']):

        start_time = twenty_four_hr_clock(time)
        start_epoch = cal_duration(start_rec, start_time) / seg_time
        end_epoch = cal_duration(start_rec, time_add(start_time, duration)) / seg_time
        if int(end_epoch) == int(start_epoch) and end_epoch <= total_epoch-1:
            label_list[int(end_epoch) + sample * total_epoch][event_dict[event]] += end_epoch - start_epoch

        else:
            for epoch in range(int(start_epoch), int(end_epoch) + 1):
                
                if epoch <= total_epoch-1:
                    if epoch < start_epoch:
                        label_list[epoch + sample * total_epoch][event_dict[event]] += (epoch + 1 - start_epoch)
                    elif end_epoch-epoch<1:
                        label_list[epoch + sample * total_epoch][event_dict[event]] += (end_epoch - epoch)
                    else:
                        label_list[epoch + sample * total_epoch][event_dict[event]] += 1

    return label_list



def threshold(start_rec, event_list, label_list, sample, threshold, seg_time):

    label_list = proportion(start_rec, event_list, label_list, sample, seg_time = seg_time)

    # x > threshold : x==1 ; x <= threshold : x == 0 
    return [int(x > threshold) for x in label_list]



def multi_class_threshold(start_rec, event_list, label_list, sample, threshold, seg_time):

    label_list = multi_class_proportion(start_rec, event_list, label_list, sample, seg_time)

    # x > threshold : x==1 ; x <= threshold : x == 0 
    return [[int(y > threshold) for y in x] for x in label_list]


def count_binary_class(labels_list):
    class_count = [0]*2
    for x in labels_list:
        class_count[x]+=1
    
    return class_count



def count_multi_class(labels_list):
    class_count = [0]*len(labels_list[0])
    for x in labels_list:
        for num in range(len(x)):
            if x[num]==1:
                class_count[num]+=1
    
    return class_count



def main(ids, start_list, csv_name, th, seg_time, type):

    assert len(ids) == len(start_list)
    # label_list = [0] * 39 * (300/seg_time) * (len(ids))

    file_name = []
    label_list = []
    for x in range(11700//seg_time * len(ids)):
        if type == 'binary':
            label_list.append(0)
        elif type == 'multi':
            label_list.append([0,0,0,0])
    


    #iterate over each id
    for sample in range(len(ids)):

        start_rec = start_list[sample]
        event_list = pd.read_csv(f'./Event_lists/{ids[sample]}_event_list.csv')
        # label_list = threshold(start_rec, event_list, label_list, sample, threshold = 0.1)


        #iterate over each event and get label
        if type == 'binary':
            label_list = threshold(start_rec, event_list, label_list, sample, threshold=th, seg_time = seg_time)
        elif type == 'multi':
            label_list = multi_class_threshold(start_rec, event_list, label_list, sample, threshold=th, seg_time = seg_time)

        #append file names for each id
        for x in range(30,69):
            for y in range(300//seg_time):
                file_name.append(f'{ids[sample]}_00{x}_{y}')


    #get dataframe and export csv
    if type == 'binary':
        df = pd.DataFrame({
            "filename" : file_name,
            "label" : label_list
        })

    elif type == 'multi':
        df = pd.concat([pd.DataFrame({"filename": file_name}), 
                        pd.DataFrame(label_list, columns=[0,1,2,3])],
                        axis=1)
        
    df.to_csv(csv_name)
    print(f'CSV File: [{csv_name}] done.')




if __name__ == "__main__":
    
    data_folder = r'/NAS/Benson/Sleep_Apnea/Sleep_Codes/Github/Sleep_Apnea/CNN_LSTM/Model_Training/Data'
    # data_folder = r'C:\Users\user\Documents\Benson\資訊\程式\Apnea_Data'
    os.chdir(data_folder)

    type = 'binary'
    seg_time = 30
    th = 0.1
    ids = ["00000712-100839", "00001118-100779", "00000782-100816", "00000711-100839", "00000781-100816", "00001096-100779", "00001097-100779"]
    start_list = ["23:54:50", "00:01:49", "23:56:56", "00:22:23", "23:57:21", "00:05:58", "00:28:05"]
    csv_name = f'{data_folder}/label_{seg_time}s_{str(int(100*th))}_{type}.csv'


    main(ids, start_list, csv_name, th, seg_time, type)
    #print(count_binary_class(pd.read_csv(csv_name)['label']))



