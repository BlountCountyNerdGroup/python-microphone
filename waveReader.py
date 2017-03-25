import wave
w = wave.open('elevatormusic.wav', 'r')
for i in range(w.getnframes()):
    frame = w.readframes(i)
    print(frame)
    print(w)