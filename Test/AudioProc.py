import librosa
import matplotlib.pyplot as plt
# from scipy.io.wavefile import write

filename = librosa.example("nutcracker")

y, samp_rate = librosa.load(filename)


plt.plot(y)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=samp_rate)

print("Estimated tempo : {:.2f} beats perminute".format(tempo))

beat_times = librosa.frames_to_time(beat_frames, sr=samp_rate)
# print(beat_times)
# plt.show()

fs = 44100
# data
# import soun
from IPython.display import Audio
# Audio(y, rate=y.size)
sr = 22050
y_sweep = librosa.chirp(fmin=librosa.note_to_hz("C3"),
                        fmax=librosa.note_to_hz("C5"),
                        sr=sr,
                        duration=1
                        )
# Audio(data=y_sweep, rate=sr)

y, sr = librosa.load(librosa.ex("trumpet"))
Audio(data=y, rate=sr)
