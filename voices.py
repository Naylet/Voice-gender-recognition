# Harmonic Product Spectrum Algorithm

from matplotlib import pylab as plt
from scipy.signal import decimate
from scipy.io import wavfile
from copy import copy
import numpy as np
import warnings
import sys
import os
import re


def analyze(file):
    print(file)

    try:
        sampling_frequency, data = wavfile.read(file)
    except ValueError:
        print("unable to read " + file)
        print("")
    else:
        if not isinstance(data[0], np.int16):
            data = data[:, 0]

        samples_count = len(data)
        audio_duration = samples_count / sampling_frequency

        data = data * np.hamming(samples_count)
        spectrum = abs(np.fft.rfft(data))
        hps = copy(spectrum)

        for q in range(2, 6):
            decimated_spectrum = decimate(spectrum, q)
            hps[:len(decimated_spectrum)] += decimated_spectrum

        peak_start = int(50 * audio_duration)
        peak = np.argmax(hps[peak_start:])
        fundamental = (peak_start + peak) / audio_duration

        #print(fundamental)

        if fundamental < 165:
            return 'M'
        else:
            return 'K'


if __name__ == "__main__":
    warnings.filterwarnings('ignore')

    if len(sys.argv) == 2:
        result = analyze("train/" + sys.argv[1])
        print(result)
        correct = re.search('([KM]).wav', sys.argv[1]).group(1)
    else:
        count_correct = 0
        filenames = os.listdir('train')

        for filename in filenames:
            result = analyze('train/' + filename)
            print(result)

            correct = re.search('([KM]).wav', filename).group(1)

            if correct == result:
                count_correct += 1

            print("")

        print("Skuteczność: %.2f%%" % (count_correct / len(filenames) * 100))
