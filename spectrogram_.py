"""Short script to visualize image in audio spectrum.

:Author:    Lukas Tycho Mendelsohn
:Date:      25/08/2021
"""

from scipy import signal
from matplotlib import pyplot as plt
import soundfile as sf
import numpy as np


audio, fs = sf.read('image_in_spec.wav')

fig = plt.figure()
ax = fig.add_subplot(111)
f, t, Sxx = signal.spectrogram(audio.sum(axis=1), fs=fs, window='hamming', nperseg=8192, noverlap=6144, scaling='spectrum', mode='magnitude')
data = 10*np.log10(Sxx)
print(data.max())
print(data.min())
ax.pcolormesh(t, f, data, cmap='turbo', shading='gouraud', vmin=-60, vmax=-15)
#ax.set_yscale('log')
ax.set_ylim(350, 2800)
ax.set_ylabel('Frequency [Hz]')
ax.set_xlabel('Time [sec]')

plt.show()