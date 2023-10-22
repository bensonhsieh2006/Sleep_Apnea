import tensorflow as tf
import numpy as np
import math
import random

class DataGenerator (tf.keras.utils.Sequence):

    def __init__(self, data, label, batch_size, patient_num, seg_time, timesteps, return_label):
        self.data = data
        self.label = label
        self.id_generator = None
        self.id_generator_2 = None
        self.batch_size = batch_size
        self.patient_num = patient_num
        self.seg_time = seg_time
        self.timesteps = timesteps
        self.return_label = return_label
        self.first_epoch = True
        self.seg_per_person = 11700//self.seg_time
        self.win_per_person = self.seg_per_person-self.timesteps+1
        self.train_size = self.patient_num*self.win_per_person
        self.step_size = self.train_size//self.batch_size

    def __len__(self):
        return math.ceil(self.train_size/self.batch_size)

    def __getitem__(self, index):
        
        # print(index)

        #handle idx=0 be sent twice from "model.fit" and "model.predict" to __getitem__()
        if self.first_epoch and index == 0:
            self.first_epoch = False
            x_batch = np.array([self.data[n:n+10] for n in range(10)])
            y_batch = np.array(self.label[9:19])

            if self.return_label:
                return x_batch, y_batch

            else:
                return x_batch

        if index == 0:
            self.id_generator = self.timestep_id_generator(self.patient_num, self.seg_per_person, self.timesteps)
            # self.id_generator_2 = self.timestep_id_generator(self.patient_num, self.seg_per_person, self.timesteps)



        if index == self.step_size:
            # print([[(m := next(self.id_generator_2)), (m+self.timesteps)]for _ in range(self.train_size-index*self.batch_size)])
            # print([(m-self.train_size+index*self.batch_size+self.timesteps), (m+self.timesteps)])

            x_batch = np.array([self.data[(n := next(self.id_generator)) : (n+self.timesteps)] for _ in range(self.train_size-index*self.batch_size)])
            y_batch = np.array(self.label[(n-self.train_size+index*self.batch_size+self.timesteps) : (n+self.timesteps)])


        elif 1 <= self.win_per_person*((index*self.batch_size)//self.win_per_person+1) - index*self.batch_size <= self.batch_size-1:
            # print([[(m := next(self.id_generator_2)), (m+self.timesteps)] for _ in range(self.batch_size)])
            # print([[m-self.batch_size+1, self.seg_per_person*((index*self.batch_size)//self.win_per_person+1)], 
            #            [self.seg_per_person*((index*self.batch_size)//self.win_per_person+1)+self.timesteps-1, m+self.timesteps]])

            x_batch = np.array([self.data[(n := next(self.id_generator)) : (n+self.timesteps)] for _ in range(self.batch_size)])
            y_batch = np.concatenate((self.label[n-self.batch_size+1 : self.seg_per_person*((index*self.batch_size)//self.win_per_person+1)],
                                      self.label[self.seg_per_person*((index*self.batch_size)//self.win_per_person+1)+self.timesteps-1 : n+self.timesteps]),
                                      axis = 0)

            
        else:
            # print([[(m := next(self.id_generator_2)), (m+self.timesteps)] for _ in range(self.batch_size)])
            # print([(m-self.batch_size+self.timesteps), (m+self.timesteps)])
   
            x_batch = np.array([self.data[(n := next(self.id_generator)) : (n+self.timesteps)] for _ in range(self.batch_size)])
            y_batch = np.array(self.label[(n-self.batch_size+self.timesteps):(n+self.timesteps)])
      
        if self.return_label:
            return x_batch, y_batch
        else:
            return x_batch            

    def on_epoch_end(self):
        pass

    def timestep_id_generator(self, num, seg_per_person, timesteps):
        for n in range(num):
            for s in range(seg_per_person-timesteps+1):
                yield n*seg_per_person+s
