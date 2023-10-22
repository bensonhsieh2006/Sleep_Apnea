import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import datetime


def offset_image(coord, name, ax):
    im = plt.imread(f'{name}.png')
    im = OffsetImage(im, zoom=0.02)
    im.image.axes = ax

    ab = AnnotationBbox(im, (-2.2, coord-0.8),  xybox=(-30., 0.), frameon=False,
                        xycoords='data',  boxcoords="offset points", pad=0)

    ax.add_artist(ab)




def plot_overall_img(label_list):
    x = [label[0] for label in label_list]
    y = [2 if label[1]==0 else 8 for label in label_list]

    start_datetime = datetime.datetime(100, 1, 1, 0, 0, 0)
    # print(start_datetime.strftime("%H:%M:%S"))

    plt.figure(figsize=(8,4), dpi=100, facecolor="#e6f3f7")
    plt.plot(x, y, color='blue')
    print([label[0] for label in label_list if label[1]==1])

    ax = plt.gca()
    ax.set_title('Sleep Apnea Continuous Detection Overall Result')

    ax.set_xlabel('Time')
    ax.xaxis.set_label_coords(1.01,-0.05)
    ax.set_xticks([label[0] for label in label_list if label[1]==1])
    ax.set_xticklabels([(start_datetime+datetime.timedelta(seconds=30*label[0])).strftime("%H:%M:%S") for label in label_list if label[1]==1])
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right', fontsize='x-small')

    ax.yaxis.set_label_coords(-0.02, 1)
    ax.set_ylabel('Label', loc='top', rotation=0)
    ax.set_ylim([0,10])
    ax.set_yticks([2,8])
    ax.set_yticklabels(['Negative', 'Positive'])

    offset_image(2, 'green_light', ax)
    offset_image(8, 'red_light', ax)

    plt.show()

if __name__ == '__main__':

    label_list = []
    for x in range(60):
        if x==13 or x==21 or x==50:
            label_list.append([x, 1])
        else:
            label_list.append([x, 0])
    plot_overall_img(label_list=label_list)