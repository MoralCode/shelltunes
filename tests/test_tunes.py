import unittest
from tunes import *

class TestTunes(unittest.TestCase):
	# def setUp(self):
	#     self.widget = Widget('The widget')

	def test_tone_to_sine_cleaninput(self):
		# 0.1 seconds of samples, should be 60 sine waves
		samples_clean = list(tone_to_sine(600, 44100, 4410 , True))
		samples = list(tone_to_sine(600, 44100, 4410, False))

		# because its a clean number of samples input, they should be the same
		self.assertEqual(samples_clean[-1], samples[-1])


	def test_tone_to_sine_messyinput(self):

		# 0.1 seconds of samples, should be 60 sine waves and 5/44100 seconds
		samples_clean = list(tone_to_sine(600, 44100, 4415 , True))
		samples = list(tone_to_sine(600, 44100, 4415, False))

		# they shouldnt end the same anymore
		self.assertNotEqual(samples_clean[-1], samples[-1])

		# project the next sample based on the last two
		projected_last_clean_sample = samples_clean[-1] + (samples_clean[-1] - samples_clean[-2])
		self.assertAlmostEqual(projected_last_clean_sample, 0, places=2)

		projected_last_nonclean_sample = samples[-1] + (samples[-1] - samples[-2])
		self.assertNotAlmostEqual(projected_last_nonclean_sample, 0, places=2)

	def test_tone_to_sine_frequency(self):

		# 0.1 seconds of samples, should be 60 sine waves
		samples = list(tone_to_sine(600, 44100, 44100, False))
		self.assertEqual(len(samples), 44100)

		# count how many times the sine wave transitions from positive to negative
		negative_swing_count = 0
		is_positive = True
		for i in samples:
			if i < 0 and is_positive:
				negative_swing_count += 1
				is_positive = False
			elif i > 0:
				is_positive = True
			else:
				pass
				# is_positive stays false
		

		self.assertEqual(negative_swing_count, 600)

if __name__ == '__main__':
    unittest.main()