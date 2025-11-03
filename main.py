import numpy
import sounddevice
import tkinter, tkinter.filedialog

dura = 1.0
samplerate = 44100

freqlist = {
    "A" : 440,
    "B" : 493.883,
    "C" : 523.251,
    "D" : 587.330,
    "E" : 659.255,
    "F" : 698.456,
    "G" : 783.991
}

root = tkinter.Tk()
root.withdraw()
fTyp = [("Musicodeファイル", "*.MSCD")]
MSCDfile = tkinter.filedialog.askopenfilename(filetypes=fTyp)
t = numpy.linspace(0, dura, int(samplerate * dura), endpoint=False)

try:
    with open(MSCDfile, "r", encoding="utf-8") as f:
        data = f.read()
        for c in data:
            try:
                wave = numpy.sin(2 * numpy.pi * freqlist[c] * t)
                sounddevice.play(wave, samplerate)
                sounddevice.wait()
                print(c)
            except Exception as e:
                print(f"Error while reading {e} in Musicode file.")
except Exception as e:
    print("File not selected")