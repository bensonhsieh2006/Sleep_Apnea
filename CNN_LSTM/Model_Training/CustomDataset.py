import tensorflow as tf
import numpy as np
import math

class DataGenerator (tf.keras.utils.Sequence):

    def __init__(self, train_data, train_label, id_generator, batch_size, patient_num, seg_time, timesteps):
        self.train_data = train_data
        self.train_label = train_label
        self.id_generator = id_generator
        self.batch_size = batch_size
        self.patient_num = patient_num
        self.seg_time = seg_time
        self.timesteps = timesteps
        self.seg_per_person = 11700//self.seg_time
        self.win_per_person = self.seg_per_person-self.timesteps+1
        self.train_size = self.patient_num*self.win_per_person
        self.step_size = self.train_size//self.batch_size

    def __len__(self):
        return math.ceil(self.train_size/self.batch_size)

    def __getitem__(self, index):
        
        if index == self.train_size//self.batch_size:
            x_batch = np.array([self.train_data[(n := next(self.id_generator)) : (n+self.timesteps)] for _ in range(self.train_size-index*self.batch_size)])
            y_batch = self.train_label[(n-self.train_size+index*self.batch_size+self.timesteps) : (n+self.timesteps)]

        elif 1 <= self.win_per_person*((index*self.batch_size)//self.win_per_person+1) - index*self.batch_size <= self.batch_size-1:
            x_batch = np.array([self.train_data[(n := next(self.id_generator)) : (n+self.timesteps)] for _ in range(self.batch_size)])
            y_batch = np.concatenate((self.train_label[n-self.batch_size+1 : self.seg_per_person*((index*self.batch_size)//self.win_per_person+1)],
                                      self.train_label[self.seg_per_person*((index*self.batch_size)//self.win_per_person+1)+self.timesteps-1 : n+self.timesteps]),
                                      axis = 0)

        else:
            x_batch = np.array([self.train_data[(n := next(self.id_generator)) : (n+self.timesteps)] for _ in range(self.batch_size)])
            y_batch = self.train_label[(n-self.batch_size+self.timesteps):(n+self.timesteps)]
            
        return x_batch, y_batch

    def on_epoch_end(self):
        pass