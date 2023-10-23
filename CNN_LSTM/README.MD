Long Short-Term Memory (LSTM) is a type of recurrent neural network (RNN) architecture that is designed to overcome the limitations of traditional RNNs in capturing long-term dependencies. LSTM networks are widely used in various fields, including natural language processing, speech recognition, and time series analysis, due to their ability to effectively model sequential data. The key feature of LSTM is its ability to selectively retain and forget information over long sequences, which is achieved through the use of specialized memory cells and gating mechanisms. This allows LSTM networks to effectively capture and utilize long-term dependencies in the input data, making them particularly suitable for tasks that involve processing and predicting sequences of data.
A unit, or cell, of an LSTM is shown in the Fig. 1, representing the process of receiving an input and producing an output in a time step. Each unit can be divided into three major blocks from left to right: the forget gate (f_t), the input gate ( i_t、C ̃_t ), and the output gate (O_t).

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/4b60c981-c8eb-4669-afa9-4fbc284b6a38)

By considering the present input (x_t), the previous state (C_(t-1)), and the output (h_(t-1)) of the unit, the classification result (y_t), state (C_t), and output (h_t) of the current unit can be obtained using the operation depicted in the figure above. The state (C_t) and output (h_t) of the current unit will be transmitted to the subsequent unit as the foundation for making predictions. The above process can be expressed in mathematical notation as follows:

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/ebef782b-dfa8-4616-92f8-71865e876569)

An LSTM network is composed of multiple units, with each unit responsible for processing a single input, calculating its own state and output, and transmitting them to the subsequent unit. By engaging in this process consistently, it attains the capability to monitor in real-time for the purpose of continuous prediction.
Convolutional Neural Network (CNN) is a type of Artificial Neural Network (ANN) that consists of convolutional layers and pooling layers. The aforementioned neural network architecture demonstrates exceptional efficacy in the extraction of features from images, rendering it extensively employed in the domains of image recognition and its associated disciplines. The convolutional layer is a crucial component in CNNs, as it employs a kernel to extract distinctive features from an image. The pooling layer is responsible for conducting down-sampling on the image, thereby reducing the dimensionality of the feature vectors and the computational complexity. CNNs possess numerous advantages, including parameter sharing, local connectivity, and translation invariance, which render them a potent tool in the realm of image processing.

The research framework of this study is illustrated in below. Initially, the collected audio data undergoes a preprocessing stage, followed by a transformation into Mel-spectrograms. Subsequently, the CNN-LSTM model is utilized to sequentially process each sample in a time-series fashion, enabling continuous prediction and facilitating real-time monitoring.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/df539aa5-6222-4f1b-a7f2-880dada418b8)





