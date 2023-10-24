 The system architecture comprises three main components: the client application, the AI algorithm and the Server Process, the Data Storage part. The Java ServerSocket framework was utilized to develop the client application, which establishes communication with the server through a web API. We also used MVC (Mode, View, Control) mechanism for the system. In the AI algorithm, we developed two models which are Hopping Window Model and Sliding Window Model. Each window employed a CNN-LSTM kernel for model training. The training data and real-time collected data were stored in a private cloud storage.

 ![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/36e0228e-749c-492f-b95d-51cb75b95654)

(1) Real-time Monitoring using the Hopping Window Model: 
In this approach, the server continuously converts audio into Mel spectrograms. When the number of stored spectrograms on the server reaches a multiple of 10, the server selects that spectrogram and the preceding 9 spectrograms as input for prediction in the model. This process generates 10 prediction values, each indicating the occurrence of symptoms related to sleep apnea within individual spectrograms, which consist of 30 seconds of audio. In essence, the model acquires audio data at regular intervals of 300 seconds and generates predictions for each 30-second segment

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/e6801134-6f5d-4640-a996-50e62b88745c)

(2) Real-time Monitoring using the Sliding Window Model: 
Once the server has accumulated 10 spectrograms, each subsequent spectrogram is fed into the model along with the preceding 9 spectrograms to generate a prediction value. This prediction indicates the manifestation of symptoms related to sleep apnea within the spectrogram, which consists of a 30-second audio recording. In other words, the model initiates the collection of audio data after 300 seconds of detection and makes predictions at intervals of 30 seconds. It combines the most recent 30 seconds of audio with the preceding 270 seconds.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/492988b1-f274-44ed-a178-2520b45ad442)

Based on the empirical findings, it is apparent that the real-time monitoring framework suggested in this investigation is operational. The client consistently transmits audio data to the server throughout its operation, while the server generates corresponding predictions at specified time intervals. Additionally, it has been noted that the model is prone to being affected by environmental noise interference during real-time monitoring, resulting in a decline in the accuracy of predictions. The current application is constrained to laboratory-level environments. In order to enhance the accuracy of predictions made by models during training, it will be imperative to integrate data that includes environmental noise interference in the future.

Both the client and server are currently being operated on computer systems. To enhance the accessibility and user-friendliness of this algorithm, there are intentions to create a mobile application for the end-user. This mobile application enables users to capture audio and transmit the data to a server for analysis, thereby serving as a more convenient method for detecting issues from the comfort of one's home.



