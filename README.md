# Sleep_Apnea
A project using deep learning to detect sleep apnea

This program introduces an intelligent mobile application that has been developed to identify sleep apnea in real-time. This is achieved through the utilization of Convolutional Neural Networks (CNN) and Long Short-Term Memory (LSTM) algorithms. In contrast to the intricate and contact polysomnography (PSG) testing that is typically employed for the diagnosis of sleep apnea, this method utilizes non-contact analysis of audio signals. This enables individuals to undergo testing in the convenience of their own homes, thereby replicating real-world conditions. Two real-time monitoring models, namely the Hopping Window Model and the Sliding Window Model, were introduced. The Sliding Window Model demonstrated a remarkable accuracy rate of up to 90% owing to its streamlined architecture. Both models have the potential to be fine-tuned in order to optimize their performance. This can be achieved by adjusting different parameters, leading to accuracy rates of 84% and 90% for each model, respectively. The study also investigated various annotation threshold settings to assess the models' capacity to detect symptoms related to sleep apnea. The highest accuracy rates of 82% and 87% were achieved at a threshold value of 0.1. The research suggests the implementation of user-friendly interfaces in the mobile application, which would facilitate seamless real-time analysis and prediction. This can be achieved by establishing a continuous transmission of audio data from the client to the server. Future advancements encompass improving the precision of the model and enhancing the accessibility and user-friendliness of the real-time monitoring algorithm by developing a mobile application for clients. This novel methodology exhibits potential for enhanced convenience and efficacy in the detection of sleep apnea, thereby potentially enhancing the quality of life for individuals afflicted by this ailment.

(A) Hopping Window Model:
This is the first version of the model employed in this study. For the audio data pertaining to the subject, this model acquires 10 spectrograms (representing 300 seconds of audio features) every 300 seconds as a single sample, thereby generating 10 distinct outputs (refer to Figure 4a). Each output indicates whether the subject displayed symptoms of sleep apnea during the 30-second interval. This study employs a "many-to-many" CNN-LSTM model, wherein each input at a given time step corresponds to a single output.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/02097002-5380-45d4-bd52-40b38bbea3db)

(B) Sliding Window Model:
This iteration represents the subsequent version of the model employed in the present investigation. In relation to the audio data of the subject, this model acquires both the current spectrogram and the preceding 9 spectrograms (current spectrogram plus the preceding 9 spectrograms) every 30 seconds as a single sample. This process yields a solitary output for the current 30-second interval (refer to Figure 5a). This output indicates whether the individual exhibited symptoms of sleep apnea within the preceding 30-second interval. Therefore, the model can be classified as a "many-to-one" model, as it generates a single output at the final time step.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/ec1d410a-f554-4660-8b2e-860ffa3a3798)

The proposed method in the Sliding window for the CNN-LSTM model utilizes multiple metrics, as shown below.
	Loss function:
Here, we use the loss function to measure the accuracy of the model. The loss is calculated by comparing the predicted value (y ̂_i) with the ground truth (y_i) each time the model makes a prediction. The accuracy of a model is determined by the smaller value of the loss function (ξ). The study utilized categorical cross entropy as the loss function. The algorithm is as follows:
ξ=-1/N  ∑_(i=1)^N▒∑_(j=1)^C▒〖y_ij  log⁡〖y ̂_ij 〗 〗                              (1)
	Optimization:
After each training iteration, the model's predictive performance can be enhanced by optimizing the loss function. The gradient descent method is utilized to minimize loss in subsequent iterations. In this study, we utilized the Adaptive Moment Estimation (Adam) algorithm as proposed in reference.
	Dropout:
To prevent overfitting during training, we incorporate Dropout into the model. Dropout deactivates some neurons with a certain probability p to achieve the effect of normalization.
	Early Stopping:
We implement Early Stopping to halt training when the validation loss of two consecutive models fails to decrease within 15/60 epochs. This approach helps prevent overfitting and improve generalization performance.
	Confusion Matrix:
      The accuracy of the final model is tested using the test set, and the test accuracy and test loss are calculated. After analyzing the test results, various metrics are calculated to provide a foundation for enhancing the model. We utilize a confusion matrix to present the final distribution of the classification results from the model. The two axes of the confusion matrix represent the predicted class and the true class, which is the ground truth. The results can be further divided into two metrics: Sensitivity and Specificity. Sensitivity indicates the accuracy of the model in predicting positive labels, while Specificity indicates the accuracy in predicting negative labels. 
	Receiver operating characteristic(ROC) curve:
In binary classification models, different threshold values are set for the predicted results. The true positive rate (TPR) and false positive rate (FPR) are calculated accordingly, and the area under the curve (AUC) is computed to evaluate the model's performance.
	Cohen's Kappa Coefficient(CKC):
The agreement between two observers on the same classification item is often used to assess the consistency between a new instrument and a standard instrument, which helps determine the accuracy of the new instrument. In this study, it is used to analyze the similarity between the annotated and predicted values.









