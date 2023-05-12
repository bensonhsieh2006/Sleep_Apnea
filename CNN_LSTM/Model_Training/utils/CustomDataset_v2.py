import tensorflow as tf
import numpy as np
import math
import random

class DataGenerator (tf.keras.utils.Sequence):

    def __init__(self, data, label, batch_size, patient_num, seg_time, timesteps, return_label):
        self.data = data
        self.label = label
        self.batch_size = batch_size
        self.patient_num = patient_num
        self.seg_time = seg_time
        self.timesteps = timesteps
        self.return_label = return_label
        self.seg_per_person = 11700//self.seg_time
        self.win_per_person = self.seg_per_person-self.timesteps+1
        self.train_size = self.patient_num*self.win_per_person
        self.step_size = self.train_size//self.batch_size
        self.timestep_list = self.timestep_id_generator(self.patient_num, self.seg_per_person, self.timesteps)

    def __len__(self):
        return math.ceil(self.train_size/self.batch_size)

    def __getitem__(self, index):

        # print(index)
        n = index * self.batch_size

        if index == self.step_size:
            # print([[self.timestep_list[n+x], self.timestep_list[n+x]+self.timesteps] for x in range(self.train_size-index*self.batch_size)])
            # print([(self.timestep_list[n+self.train_size-index*self.batch_size-1]-self.train_size+index*self.batch_size+self.timesteps),  (self.timestep_list[n+self.train_size-index*self.batch_size-1]+self.timesteps)])

            x_batch = np.array([self.data[self.timestep_list[n+x]: self.timestep_list[n+x]+self.timesteps] for x in range(self.train_size-index*self.batch_size)])
            y_batch = np.array(self.label[(self.timestep_list[n+self.train_size-index*self.batch_size-1]-self.train_size+index*self.batch_size+self.timesteps) : (self.timestep_list[n+self.train_size-index*self.batch_size-1]+self.timesteps)])


        elif 1 <= self.win_per_person*((index*self.batch_size)//self.win_per_person+1) - index*self.batch_size <= self.batch_size-1:
            # print([[self.timestep_list[n+x], self.timestep_list[n+x]+self.timesteps] for x in range(self.batch_size)])
            # print([[self.timestep_list[n+self.batch_size-1]-self.batch_size+1, self.seg_per_person*((index*self.batch_size)//self.win_per_person+1)], 
            #        [self.seg_per_person*((index*self.batch_size)//self.win_per_person+1)+self.timesteps-1, self.timestep_list[n+self.batch_size-1]+self.timesteps]])

            x_batch = np.array([self.data[self.timestep_list[n+x]: self.timestep_list[n+x]+self.timesteps] for x in range(self.batch_size)])
            y_batch = np.concatenate((self.label[self.timestep_list[n+self.batch_size-1]-self.batch_size+1 : self.seg_per_person*((index*self.batch_size)//self.win_per_person+1)],
                                      self.label[self.seg_per_person*((index*self.batch_size)//self.win_per_person+1)+self.timesteps-1 : self.timestep_list[n+self.batch_size-1]+self.timesteps]),
                                      axis = 0)

            
        else:
            # print([[self.timestep_list[n+x], self.timestep_list[n+x]+self.timesteps] for x in range(self.batch_size)])
            # print([(self.timestep_list[n+self.batch_size-1]-self.batch_size+self.timesteps), (self.timestep_list[n+self.batch_size-1]+self.timesteps)])
   
            x_batch = np.array([self.data[self.timestep_list[n+x]: self.timestep_list[n+x]+self.timesteps] for x in range(self.batch_size)])
            y_batch = np.array(self.label[(self.timestep_list[n+self.batch_size-1]-self.batch_size+self.timesteps):(self.timestep_list[n+self.batch_size-1]+self.timesteps)])
      
        if self.return_label:
            return x_batch, y_batch
        else:
            return x_batch    


    def on_epoch_end(self):
        pass

    def timestep_id_generator(self, num, seg_per_person, timesteps):
        timestep_list = []
        for n in range(num):
            for s in range(seg_per_person-timesteps+1):
                timestep_list.append(n*seg_per_person+s)

        return timestep_list
