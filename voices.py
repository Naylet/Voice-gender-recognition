# Harmonic Product Spectrum Algorithm

#fft - decimate(2:6)-fundamental

from matplotlib import pylab as plt
import numpy as np
from scipy.io import wavfile
import soundfile
import sys
import os


def open(file):
    print("opening " + file)

    try:
        signal, sample_rate = soundfile.read(file)
    except ValueError:
        print("unable to read " + file)
        print("")
    else:
        print(sample_rate)
        plt.plot(signal)
        plt.show()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        open("train/" + sys.argv[1])
    else:
        filenames = os.listdir('train')

        file_number = len(filenames)
        checked_positive = 0

        for filename in filenames:
            open('train/' + filename)
