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
(1) Loss function:
Here, we use the loss function to measure the accuracy of the model. The loss is calculated by comparing the predicted value (y ̂_i) with the ground truth (y_i) each time the model makes a prediction. The accuracy of a model is determined by the smaller value of the loss function (ξ). The study utilized categorical cross entropy as the loss function. The algorithm is as follows:

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/2b7cf5a1-8e79-404d-98ac-cc457a74d5af)

(2) Optimization:
After each training iteration, the model's predictive performance can be enhanced by optimizing the loss function. The gradient descent method is utilized to minimize loss in subsequent iterations. In this study, we utilized the Adaptive Moment Estimation (Adam) algorithm as proposed in reference.
(3) Dropout:
To prevent overfitting during training, we incorporate Dropout into the model. Dropout deactivates some neurons with a certain probability p to achieve the effect of normalization.
(3) Early Stopping:
We implement Early Stopping to halt training when the validation loss of two consecutive models fails to decrease within 15/60 epochs. This approach helps prevent overfitting and improve generalization performance.
(4) Confusion Matrix:
The accuracy of the final model is tested using the test set, and the test accuracy and test loss are calculated. After analyzing the test results, various metrics are calculated to provide a foundation for enhancing the model. We utilize a confusion matrix to present the final distribution of the classification results from the model. The two axes of the confusion matrix represent the predicted class and the true class, which is the ground truth. The results can be further divided into two metrics: Sensitivity and Specificity. Sensitivity indicates the accuracy of the model in predicting positive labels, while Specificity indicates the accuracy in predicting negative labels. 
(5) Receiver operating characteristic(ROC) curve:
In binary classification models, different threshold values are set for the predicted results. The true positive rate (TPR) and false positive rate (FPR) are calculated accordingly, and the area under the curve (AUC) is computed to evaluate the model's performance.
(6) Cohen's Kappa Coefficient(CKC):
The agreement between two observers on the same classification item is often used to assess the consistency between a new instrument and a standard instrument, which helps determine the accuracy of the new instrument. In this study, it is used to analyze the similarity between the annotated and predicted values.

For the real-time monitoring models proposed in this study, the training results of the models were obtained by adjusting the neural network layer composition and various parameters. The model's performance will be presented using tables and line charts, which will include accuracy, loss value, and several indicators: training accuracy (Train_acc), training loss (Train_loss), validation accuracy (Val_acc), validation loss (Val_loss), test accuracy (Test_acc), test loss (Test_loss), area under the ROC curve (ROC_AUC), and Cohen's Kappa Coefficient (CKC). A total of 8 items will be compared.

(a).The Impact of Different Dropout on Training Results
To prevent overfitting during model training, this study incorporated Dropout into the later layers of the model, which randomly disables neurons with a certain probability. The table below shows the results of testing different dropout probabilities. From the table, it is evident that when the dropout probability is set to 0.1, the test accuracy reaches 90.00% and the ROC_AUC reaches 0.9680, surpassing the other 7 tested dropout probabilities.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/fc69e47c-cbcb-40d3-8f2a-742f27c329bd)

The results in Figure 6 show that a dropout value of 0.1 leads to higher accuracy and better performance in both metrics, as well as lower loss. Meanwhile, it also achieves the highest ROC_AUC and CKC values when the dropout value is set to 0.1.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/bb7a7d1f-798b-443a-85db-eb1156f1591c)

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/39922c64-ffe7-4054-b57f-ff727ecb3c8c)

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/850191a7-0580-4e61-8a35-b39492fc2e34)

(b) The Impact of Different Label Threshold on Training Results
The table shows that setting the threshold values at 0.05 and 0.1 improved the performance of the model. The test accuracies were 88.49% and 87.00%, with corresponding ROC_AUC values of 0.9410 and 0.9280. As the threshold value increased, the model's performance gradually decreased. However, this trend was less pronounced, indicating that the model has a stronger ability to differentiate and can utilize more data from the sample.

The table shows that setting the threshold values at 0.05 and 0.1 improved the performance of the model. The test accuracies were 88.49% and 87.00%, with corresponding ROC_AUC values of 0.9410 and 0.9280. As the threshold value increased, the model's performance gradually decreased. However, this trend was less pronounced, indicating that the model has a stronger ability to differentiate and can utilize more data from the sample.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/c055db61-15c0-4c32-84af-827e7770bf26)

The figure below demonstrates that setting the threshold value to 0.1 results in higher accuracy and scores for both metrics, while also minimizing the loss value. This indicates that the model achieves optimal performance during training with this threshold value.
Figure 7 illustrates the relationship between the threshold value and the accuracy rate, loss rate, AUC_ROC, and CKC values.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/19c1dec8-efc9-4135-a6df-f0ba307bc10e)

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/73dee455-9f89-4dbf-b569-8b49437c8ea1)

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/3cd3cb0b-0299-47fd-8731-785b5f0e9957)

(c) Optimal Parameters
Based on experiments with various parameters and annotation thresholds, we have obtained the optimal results achievable by the sliding window model. The data is presented below:
•	Number samples= 1524 (Training:Validation:Testing = 1174:150:200
•	Number epoch = 439
•	Batch size = 10
•	Learning rate = 0.00001
•	Dropout(p) = 0.1
•	Label Threshold = 0.1
The learning curves in Figure 8 illustrate that the training and validation loss decrease with an increasing number of training epochs. Eventually, they stabilize with minor fluctuations at values of 0.1918 and 0.2166, respectively.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/18b82cd0-7899-46df-b299-5fad53344c48)

(d)Testing Results: 
The examination of the confusion matrix reveals that the model exhibits a significant level of precision in forecasting the majority of label values, with 9 occurrences of false negatives and 15 occurrences of false positives. The sensitivity and specificity values are reported as 0.87 and 0.81, respectively. Additionally, the ROC curve analysis yielded an area under the curve (AUC) value of 0.8925, as illustrated in below image.

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/f8c44b24-6af2-402a-b64c-ff5e3af692cb)



















