import pandas as pd



def twenty_four_hr_clock(time):
    if time[:2] == "下午":
        return str(int(time[3:5])+12)+time[5:]
    elif time[3:5] == "12":
        return str(int(time[3:5])-12)+'0'+time[5:]
    else:
        return time[3:]



def time_add(t1, sec):
    hr1, min1, sec1 = int(t1[:2]), int(t1[3:5]), int(t1[6:8])

    time_sec = int((sec1+sec)%60)
    time_min = int((min1+(sec1+sec)//60)%60)
    time_hr = int((hr1+(min1+(sec1+sec)//60)//60)%12)
    time = f'{time_hr}:{time_min}:{time_sec}'
    if time_hr<10:
        time = f'0{time}'
    if time_min<10:
        time = f'{time[:3]}0{time[3:]}'
    if time_sec<10:
        time = f'{time[:6]}0{time[6:]}'

    return time


#outputs (t2-t1) in seconds
def cal_duration(t1, t2):
    hr1, min1, sec1 = int(t1[:2]), int(t1[3:5]), int(t1[6:8])
    hr2, min2, sec2 = int(t2[:2]), int(t2[3:5]), int(t2[6:8]) 

    time_sec = (sec2-sec1+60)%60
    time_min = (min2-min1-(sec1>sec2)+60)%60
    time_hr = (hr2-hr1-(min1>min2-(sec1>sec2))+24)%24
    return time_hr*3600+time_min*60+time_sec 


def main():
    ids = ["00000711-100839", "00000781-100816"]
    start_list = ["00:22:23", "23:57:21"]
    num_list = [0]*390*len(ids)
    file_name = []

    for step in range(len(ids)):   
        start_rec = start_list[step]
        event_list = pd.read_csv(f'{ids[step]}_event_list.csv')

        for time, duration in zip(event_list['Time'], event_list['Duration']):
            start_time = twenty_four_hr_clock(time)
            for x in range(int(duration/30)+1):
                epoch = int(cal_duration(start_rec, time_add(start_time, x*30))/30)
                if epoch<=389:
                    num_list[epoch+step*390]=1
            
            epoch = int(cal_duration(start_rec, time_add(start_time, duration))/30)
            if epoch<=389:
                num_list[epoch+step*390]=1
        
        for x in range(30,69):
            for y in range(10):
                file_name.append(f'{ids[step]}_00{x}_{y}')

    label = {
        "filename" : file_name,
        "label" : num_list
    }
    print(len(label['filename']))
    print(len(label['label']))
    df = pd.DataFrame(label)
    df.to_csv('label.csv')



if __name__ == "__main__":
    main()



# [0,0,0,0,1,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,
# 0,0,1,1,1,1,1,1,1,1,
# 1,1,1,1,1,1,1,1,0,0,
# 0,1,1,1,0,0,0,0,1,1,
# 1,1,1,1,1,1,1,1,1,1,
# 1,1,1,1,1,0,1,1,0,0,
# 0,0,0,0,1,1,1,1,1,1,
# 1,1,1,1,1,0,0,0,0,0,
# 0,0,1,1,1,1,0,0,0,0,
# 0,1,1,0,0,0,0,0,1,1,
# 1,1,1,0,0,0,1,0,1,1,
# 1,1,1,1,1,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,0,0,0,
# 0,0,0,0,0,0,0,1,1,1
# ]