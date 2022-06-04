import sys
import wave

# modified From: https://stackoverflow.com/questions/16111038/how-to-convert-pcm-files-to-wav-files-scripting
for arg in sys.argv[1:]:
	with open(arg, 'rb') as pcmfile:
		pcmdata = pcmfile.read()
	with wave.open(arg+'.wav', 'wb') as wavfile:
		# (nchannels, sampwidth, framerate, nframes, comptype, compname)
		framerate = 24000
		wavfile.setparams((2, 2, framerate, 0, 'NONE', 'NONE'))
		wavfile.writeframes(pcmdata)