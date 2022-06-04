import sys
import math

# https://www.daniweb.com/programming/software-development/threads/354944/creating-a-sine-wave-at-a-specific-frequency-and-sample-rate
def tone_to_sine(frequency:int, samplerate: int, duration:int, clean_end: bool):
	"""converts a frequency to a sine wave at that frequency

	Args:
		frequency (int): number of oscilations per second
		samplerate (int): number of samples in a second
		duration (int): number of samples worth of data to generate
		clean_end (bool): cuts the output slightly short such that it ends at/near a complete cycle. this eliminates popping between tones

	Yields:
		double: samples of the sine wave
	"""
	if clean_end:
		samples_per_cycle=samplerate/frequency
		total_cycles = duration/samples_per_cycle
		complete_cycles = math.floor(total_cycles)
		samplecount = int(complete_cycles * samples_per_cycle)
	else:
		samplecount = duration

	for i in range(samplecount):
		yield math.sin((frequency * (2* math.pi) * i) / samplerate)


if __name__ == '__main__':
	for line in sys.stdin:
		pass