hr = 23
minute = 57
sec = 21


samples = 39
timesteps = 10
sec_per_timestep = 30

for x in range(samples):
    for y in range(timesteps):
        
        minute += int((sec+sec_per_timestep)//60)
        sec = (sec+sec_per_timestep)%60

        hr += int(minute//60)
        minute = minute%60

        time = f'{hr}:{minute}:{sec}'
        if hr<10:
            time = f'0{time}'
        if minute<10:
            time = f'{time[:3]}0{time[3:]}'
        if sec<10:
            time = f'{time[:6]}0{time[6:]}'

        print(time, end=' ')
    print()        
