import librosa
from librosa import display
import matplotlib as mpl
import matplotlib.pyplot as plt
import gc
import stat
import os
from pydub import AudioSegment
import moviepy.editor as mp
from memory_profiler import profile
import time
import sys
#AudioSegment.ffprobe = r'/home/why/anaconda3/lib/python3.9/site-packages/ffprobe/ffprobe.py'

#os.environ["PATH"] += os.pathsep + r'/home/why/anaconda3/lib/python3.9/site-packages'
#print(os.environ['PATH'])
#os.chmod(r'/home/why/anaconda3/lib/python3.9/site-packages/ffprobe/ffprobe.py', stat.S_IRWXU)


def transfer(source_path, dest_path):

    my_clip = mp.VideoFileClip(source_path)
    my_clip.audio.write_audiofile(dest_path)


def CombineWav(files, new_path):
    combined = AudioSegment.empty()
    for file in files:
        sound = AudioSegment.from_file(file,format="wav")
        combined += sound

    combined.export(f"{new_path}/combined.wav", format="wav")
    print(f"{new_path}/combined.wav: Finished")



def mel(output_name, y, sr): 
    fmax = 8192
    output_path = output_name + ".png"
    
    melspec = librosa.feature.melspectrogram(y,sr,
                                    n_mels=256,
                                    n_fft=8192,
                                    fmax=fmax)
    logmelspec = librosa.power_to_db(melspec)

    # mel spectrogram
    fig,ax = plt.subplots()
    img = display.specshow(logmelspec, cmap='magma', sr=sr,                         
                         fmax=fmax, ax=ax)
    cbar = fig.colorbar(img)
    cbar.mappable.set_clim(-40, 40)
    cbar.remove()
    plt.savefig(output_path)
    plt.close()
    
    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()



def mfcc(ori_path, new_path):
    mpl.use('agg')
    input_name = ori_path + '.wav'
    output_name = new_path + ".png"

    y,sr = librosa.load(input_name,sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=256)

    img = display.specshow(mfccs, x_axis='time')
    plt.colorbar(img)
    plt.clim(-500, 300)
    plt.title('MFCC')
    plt.savefig(output_name)
    plt.close()
    
    for x in list(locals().keys())[:]:
        del locals()[x]
    gc.collect()

    print(output_name + ": Finished")