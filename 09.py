'''
Created by Roman Beya
Created on 24-oct-2017
Created for ICS3U
This program displays the alphabet with it's corresponding lower case for every CAPITAL & LOWERCASE letter in the alphabet
'''
for outer_counter in range(65, 91): # all CAPITAL letters of alphabet
	for inner_counter in range(97, 123): # all LOWERCASE letters of alphabet
		print unichr(outer_counter) + "->" + unichr(inner_counter)
