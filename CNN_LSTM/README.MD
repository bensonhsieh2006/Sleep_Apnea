Long Short-Term Memory (LSTM) is a type of recurrent neural network (RNN) architecture that is designed to overcome the limitations of traditional RNNs in capturing long-term dependencies. LSTM networks are widely used in various fields, including natural language processing, speech recognition, and time series analysis, due to their ability to effectively model sequential data. The key feature of LSTM is its ability to selectively retain and forget information over long sequences, which is achieved through the use of specialized memory cells and gating mechanisms. This allows LSTM networks to effectively capture and utilize long-term dependencies in the input data, making them particularly suitable for tasks that involve processing and predicting sequences of data.
A unit, or cell, of an LSTM is shown in the Fig. 1, representing the process of receiving an input and producing an output in a time step. Each unit can be divided into three major blocks from left to right: the forget gate (f_t), the input gate ( i_t、C ̃_t ), and the output gate (O_t).

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/4b60c981-c8eb-4669-afa9-4fbc284b6a38)



