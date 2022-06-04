import sys
import math

# https://www.daniweb.com/programming/software-development/threads/354944/creating-a-sine-wave-at-a-specific-frequency-and-sample-rate
def tone_to_sine(frequency:int, samplerate: int, duration:int):
	"""converts a frequency to a sine wave at that frequency

	Args:
		frequency (int): number of oscilations per second
		samplerate (int): number of samples in a second
		duration (int): number of samples worth of data to generate

	Yields:
		double: samples of the sine wave
	"""
	for i in range(duration):
		yield math.sin((frequency * (2* math.pi) * i) / samplerate)



for line in sys.stdin:
	pass