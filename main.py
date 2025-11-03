import numpy
import sounddevice

freq = 440
dura = 1.0
samplerate = 44100

t = numpy.linspace(0, dura, int(samplerate * dura), endpoint=False)
wave = numpy.sin(2 * numpy.pi * freq * t)

sounddevice.play(wave, samplerate)
sounddevice.wait()