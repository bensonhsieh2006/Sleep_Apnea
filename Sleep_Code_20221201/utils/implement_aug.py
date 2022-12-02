import librosa
import librosa.display
import soundfile as sf
import matplotlib.pyplot as plt
import audiomentations as am
import gc



def Add_Gaussian_Noise(ori_path, new_path):

    input_name = ori_path + ".wav"
    output_name_1 = new_path + "_add_gaussian_noise.wav"
    output_name_2 = new_path + "_add_gaussian_noise.png"


    y,sr = librosa.load(input_name,sr=None)
    augment = am.AddGaussianNoise()
    agumented_signal = augment(samples=y, sample_rate=sr)



    fig, (ax1,ax2) = plt.subplots(2,1)

    img1 = librosa.display.waveshow(y=y,sr=sr,x_axis='time',ax=ax1)
    ax1.set(title='Before')

    img2 = librosa.display.waveshow(y=agumented_signal,sr=sr,x_axis='time',ax=ax2)
    ax2.set(title='After')

    plt.tight_layout()
    plt.savefig(output_name_2)
    plt.close()


    sf.write(output_name_1,agumented_signal,sr)

    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()




def Add_Background_Noise(ori_path, new_path, sound_path):
    print(sound_path)
    input_name = ori_path + ".wav"
    output_name_1 = new_path + "_add_background_noise.wav"
    output_name_2 = new_path + "_add_background_noise.png"



    y,sr = librosa.load(input_name,sr=None)
    augment = am.AddBackgroundNoise(sounds_path = sound_path)
    agumented_signal = augment(samples=y,sample_rate = sr)



    fig, (ax1,ax2) = plt.subplots(2,1)

    img1 = librosa.display.waveshow(y=y,sr=sr,x_axis='time',ax=ax1)
    ax1.set(title='Before')

    img2 = librosa.display.waveshow(y=agumented_signal,sr=sr,x_axis='time',ax=ax2)
    ax2.set(title='After')

    plt.tight_layout()
    plt.savefig(output_name_2)
    plt.close()

    sf.write(output_name_1,agumented_signal,sr)

    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()




def Add_Short_Noises(ori_path, new_path, sound_path):
    input_name = ori_path + ".wav"
    output_name_1 = new_path + "_add_short_noises.wav"
    output_name_2 = new_path + "_add_short_noises.png"


    y,sr = librosa.load(input_name,sr=None)
    augment = am.AddShortNoises(sounds_path  = sound_path)
    agumented_signal = augment(samples=y,sample_rate = sr)



    fig, (ax1,ax2) = plt.subplots(2,1)

    img1 = librosa.display.waveshow(y=y,sr=sr,x_axis='time',ax=ax1)
    ax1.set(title='Before')

    img2 = librosa.display.waveshow(y=agumented_signal,sr=sr,x_axis='time',ax=ax2)
    ax2.set(title='After')

    plt.tight_layout()
    plt.savefig(output_name_2)
    plt.close()



    sf.write(output_name_1,agumented_signal,sr)
    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()




def Band_Pass_Filter(ori_path, new_path):
    input_name = ori_path + ".wav"
    output_name_1 = new_path + "_band_pass_filter.wav"
    output_name_2 = new_path + "_band_pass_filter.png"



    y,sr = librosa.load(input_name,sr=None)
    augment = am.BandPassFilter()
    agumented_signal = augment(samples=y,sample_rate = sr)



    fig, (ax1,ax2) = plt.subplots(2,1)

    img1 = librosa.display.waveshow(y=y,sr=sr,x_axis='time',ax=ax1)
    ax1.set(title='Before')

    img2 = librosa.display.waveshow(y=agumented_signal,sr=sr,x_axis='time',ax=ax2)
    ax2.set(title='After')

    plt.tight_layout()
    plt.savefig(output_name_2)
    plt.close()



    sf.write(output_name_1,agumented_signal,sr)
    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()




def High_Pass_Filter(ori_path, new_path):
    input_name = ori_path + ".wav"
    output_name_1 = new_path + "_high_pass_filter.wav"
    output_name_2 = new_path + "_high_pass_filter.png"



    y,sr = librosa.load(input_name,sr=None)
    augment = am.HighPassFilter()
    agumented_signal = augment(samples=y,sample_rate = sr)



    fig, (ax1,ax2) = plt.subplots(2,1)

    img1 = librosa.display.waveshow(y=y,sr=sr,x_axis='time',ax=ax1)
    ax1.set(title='Before')

    img2 = librosa.display.waveshow(y=agumented_signal,sr=sr,x_axis='time',ax=ax2)
    ax2.set(title='After')

    plt.tight_layout()
    plt.savefig(output_name_2)
    plt.close()



    sf.write(output_name_1,agumented_signal,sr)
    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()




def Low_Pass_Filter(ori_path, new_path):
    input_name = ori_path + ".wav"
    output_name_1 = new_path + "_low_pass_filter.wav"
    output_name_2 = new_path + "_low_pass_filter.png"



    y,sr = librosa.load(input_name,sr=None)
    augment = am.LowPassFilter()
    agumented_signal = augment(samples=y,sample_rate = sr)



    fig, (ax1,ax2) = plt.subplots(2,1)

    img1 = librosa.display.waveshow(y=y,sr=sr,x_axis='time',ax=ax1)
    ax1.set(title='Before')

    img2 = librosa.display.waveshow(y=agumented_signal,sr=sr,x_axis='time',ax=ax2)
    ax2.set(title='After')

    plt.tight_layout()
    plt.savefig(output_name_2)
    plt.close()


    sf.write(output_name_1,agumented_signal,sr)
    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()




def Frequency_Mask(ori_path, new_path):
    input_name = ori_path + ".wav"
    output_name_1 = new_path + "_frequency_mask.wav"
    output_name_2 = new_path + "_frequency_mask.png"



    y,sr = librosa.load(input_name,sr=None)
    augment = am.FrequencyMask()
    agumented_signal = augment(samples=y,sample_rate = sr)



    fig, (ax1,ax2) = plt.subplots(2,1)

    img1 = librosa.display.waveshow(y=y,sr=sr,x_axis='time',ax=ax1)
    ax1.set(title='Before')

    img2 = librosa.display.waveshow(y=agumented_signal,sr=sr,x_axis='time',ax=ax2)
    ax2.set(title='After')

    plt.tight_layout()
    plt.savefig(output_name_2)
    plt.close()


    sf.write(output_name_1,agumented_signal,sr)
    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()




def Time_Mask(ori_path, new_path):
    input_name = ori_path + ".wav"
    output_name_1 = new_path + "_time_mask.wav"
    output_name_2 = new_path + "_time_mask.png"



    y,sr = librosa.load(input_name,sr=None)
    augment = am.TimeMask()
    agumented_signal = augment(samples=y,sample_rate = sr)



    fig, (ax1,ax2) = plt.subplots(2,1)

    img1 = librosa.display.waveshow(y=y,sr=sr,x_axis='time',ax=ax1)
    ax1.set(title='Before')

    img2 = librosa.display.waveshow(y=agumented_signal,sr=sr,x_axis='time',ax=ax2)
    ax2.set(title='After')

    plt.tight_layout()
    plt.savefig(output_name_2)
    plt.close()


    sf.write(output_name_1,agumented_signal,sr)
    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()




def Reverse(ori_path, new_path):
    input_name = ori_path + ".wav"
    output_name_1 = new_path + "_reverse.wav"
    output_name_2 = new_path + "_reverse.png"



    y,sr = librosa.load(input_name,sr=None)
    augment = am.Reverse()
    agumented_signal = augment(samples=y,sample_rate = sr)



    fig, (ax1,ax2) = plt.subplots(2,1)

    img1 = librosa.display.waveshow(y=y,sr=sr,x_axis='time',ax=ax1)
    ax1.set(title='Before')

    img2 = librosa.display.waveshow(y=agumented_signal,sr=sr,x_axis='time',ax=ax2)
    ax2.set(title='After')

    plt.tight_layout()
    plt.savefig(output_name_2)
    plt.close()


    sf.write(output_name_1,agumented_signal,sr)
    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()




def Shift(ori_path, new_path):
    input_name = ori_path + ".wav"
    output_name_1 = new_path + "_shift.wav"
    output_name_2 = new_path + "_shift.png"



    y,sr = librosa.load(input_name,sr=None)
    augment = am.Shift()
    agumented_signal = augment(samples=y,sample_rate = sr)



    fig, (ax1,ax2) = plt.subplots(2,1)

    img1 = librosa.display.waveshow(y=y,sr=sr,x_axis='time',ax=ax1)
    ax1.set(title='Before')

    img2 = librosa.display.waveshow(y=agumented_signal,sr=sr,x_axis='time',ax=ax2)
    ax2.set(title='After')

    plt.tight_layout()
    plt.savefig(output_name_2)
    plt.close()


    sf.write(output_name_1,agumented_signal,sr)
    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()
