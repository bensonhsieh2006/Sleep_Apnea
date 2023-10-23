The study utilizes a combination of CNN and LSTM architecture. The spectrogram of each time step is initially processed by a CNN. The resulting image features are then flattened and inputted into an LSTM for prediction, as shown in below image. The proposed model is based on the combination of convolutional neural networks (CNN) and audio data, taking into account the time series nature of the data and the temporal correlation between data. This combination is chosen due to the suitability of CNN for image classification.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/1a21cf67-6bdb-4237-99d1-abe69ffc5652)

We propose Sliding Window models for real-time monitoring and detection of sleep apnea using continuous audio input. Both real-time monitoring models consist of a 10-unit CNN-LSTM neural network, which spans 10 time steps. The Sliding Window model uses 10 spectrograms as input, with each spectrogram recording the audio features of a 30-second segment. The spectrograms of each sample are input sequentially into the CNN. The feature information obtained is then input into each unit of the LSTM to obtain the final output result Fig. 5.
The data and their annotations were divided into three parts: Training Set, Validation Set, and Testing Set. These sets were then used to train the real-time monitoring models with different numbers of epochs. During training, the model was fed large batches of data, with the batch size determining the number of samples processed in each iteration. After each epoch, the accuracy and loss during training were calculated. The model's performance during training was evaluated by computing the validation accuracy and loss using the validation set. 

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/90ce06e7-6cf0-46b2-b89a-20727de151fa)



