The study recorded 500 minutes of audio data from each subject per night. We collected data for a total of 195 minutes, specifically from the 150th to the 345th minute. The data was divided into 30-second intervals, resulting in 390 audio segments for each subject.
We transformed the audio segments from the previous step into Mel Spectrograms, as depicted in below image. Mel spectrograms replicate the non-linear perception of sound by the human ear. The frequency-related coefficients are calculated using the Short Time Fourier Transform (STFT) to extract frequency-related coefficients. Each frame in the frequency domain is processed through a Mel Filter Bank to extract the necessary information. The conversion between Hertz (f) and Mel (m) is defined as follows:  m=2595*(1+700f)

![image](https://github.com/bensonhsieh2006/Sleep_Apnea/assets/52516956/edb2db46-6f56-4ceb-9730-269262053fc5)

