import sys
import math
import random



def rand_to_note_special(rand):
	"""converts a random integer to a note
	"""
	notes = [4, 5, 7, 11]
	note_index = rand % 8
	if note_index > len(notes) -1:
		note = 0
	else:
		note = notes[note_index]/12
	note = note * math.log(2)
	note = math.exp(note)
	note = note*1046

	return note



def rand_to_note(rand):
	"""converts a random integer to a note
	"""
	notes = [600, 800, 1000, 1200]
	note_index = rand % len(notes) -1
	if note_index > len(notes) -1:
		note = 400 # default note
	else:
		note = notes[note_index]

	return note

def note_to_frequency_special(note):
	# this junk negates the math in tone_to_sine to get to a frequency value
	note = note*samplerate/(2*math.pi)
	return note




# https://www.daniweb.com/programming/software-development/threads/354944/creating-a-sine-wave-at-a-specific-frequency-and-sample-rate
def tone_to_sine(frequency:int, samplerate: int, samples:int, clean_end: bool):
	"""converts a frequency to a sine wave at that frequency.

	Args:
		frequency (int): number of oscilations per second
		samplerate (int): number of samples in a second
		samples (int): number of samples worth of data to generate
		clean_end (bool): cuts the output slightly short such that it ends at/near a complete cycle. this eliminates popping between tones

	Yields:
		double: samples of the sine wave
	"""
	if clean_end:
		samples_per_cycle=samplerate/frequency
		total_cycles = (samples)/samples_per_cycle
		complete_cycles = math.floor(total_cycles)
		samplecount = int(complete_cycles * samples_per_cycle)
	else:
		samplecount = samples
	
	for i in range(samplecount):
		yield math.sin((frequency * (2* math.pi) * i) / samplerate)

def apply_volume(generator, vol=100):
	for i in generator:
		yield int(vol * i)



if __name__ == '__main__':
	samplerate = 48000
	note_duration = 1*samplerate
	# while True:
	randint = random.randint(0, 255)
	note = rand_to_note(randint, samplerate)
	freq = note_to_frequency_special(note)
	for i in apply_volume(tone_to_sine(freq, samplerate, note_duration, True)):
		print(i.to_bytes(4, byteorder='big', signed=True).hex())
