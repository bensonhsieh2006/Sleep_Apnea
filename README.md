# Sleep_Apnea
A project using deep learning to detect sleep apnea

This program introduces an intelligent mobile application that has been developed to identify sleep apnea in real-time. This is achieved through the utilization of Convolutional Neural Networks (CNN) and Long Short-Term Memory (LSTM) algorithms. In contrast to the intricate and contact polysomnography (PSG) testing that is typically employed for the diagnosis of sleep apnea, this method utilizes non-contact analysis of audio signals. This enables individuals to undergo testing in the convenience of their own homes, thereby replicating real-world conditions. Two real-time monitoring models, namely the Hopping Window Model and the Sliding Window Model, were introduced. The Sliding Window Model demonstrated a remarkable accuracy rate of up to 90% owing to its streamlined architecture. Both models have the potential to be fine-tuned in order to optimize their performance. This can be achieved by adjusting different parameters, leading to accuracy rates of 84% and 90% for each model, respectively. The study also investigated various annotation threshold settings to assess the models' capacity to detect symptoms related to sleep apnea. The highest accuracy rates of 82% and 87% were achieved at a threshold value of 0.1. The research suggests the implementation of user-friendly interfaces in the mobile application, which would facilitate seamless real-time analysis and prediction. This can be achieved by establishing a continuous transmission of audio data from the client to the server. Future advancements encompass improving the precision of the model and enhancing the accessibility and user-friendliness of the real-time monitoring algorithm by developing a mobile application for clients. This novel methodology exhibits potential for enhanced convenience and efficacy in the detection of sleep apnea, thereby potentially enhancing the quality of life for individuals afflicted by this ailment.

 The system architecture comprises three main components: the client application, the AI algorithm and the Server Process, the Data Storage part. The Java ServerSocket framework was utilized to develop the client application, which establishes communication with the server through a web API. We also used MVC (Mode, View, Control) mechanism for the system. In the AI algorithm, we developed two models which are Hopping Window Model and Sliding Window Model. Each window employed a CNN-LSTM kernel for model training. The training data and real-time collected data were stored in a private cloud storage (Figure 1).

 ![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/36e0228e-749c-492f-b95d-51cb75b95654)



![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/4b60c981-c8eb-4669-afa9-4fbc284b6a38)



