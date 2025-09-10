from mido import *
import sys

#read midi from file
midi_source_file = sys.argv[1] #if error here: missing midi file argument? try "python midiToTab.py YOUR_MIDI_FILE.mid"
mid = MidiFile(midi_source_file)

#define a guitar's standard tuning in terms of midi-notes
	#["E2","A2","D3","G3","B4","E4"]
strings = [40, 45, 50, 55, 59, 64]
numFrets = 22

#------------------------------------------------
def lengthen_empty_lines(tab: list):
	"""
	assumes all list items are strings.
	adds "-" to the end of every item until all items are the same length.
	"""
	max = 0
	for line in tab:
		if len(line) > max:
			max = len(line)
	for i, line in enumerate(tab):
		if len(line) < max:
			length_difference = max - len(line)
			filler = "-" * length_difference
			tab[i] += filler
	#test: for line in tab: len(line) == max		
	
#------------------------------------------------

for i, track in enumerate(mid.tracks):
	print('Track {}: {}'.format(i, track.name))

for i, track in enumerate(mid.tracks):
	#tab[0] is High E, tab[5] is Low E
	tab = ["|","|","|","|","|","|"]
	
	track_bad_flag = True #most tracks dont have notes
	for msg in track:
		#print(msg)
		#print(msg.type)
		if msg.type == 'note_on':
			track_bad_flag= False
			#first approach: find the leftmost-place to play each note
			if msg.note < strings[0]:
				#print(msg)
				#print('message too low to add to tab')
				track_bad_flag = True
			elif msg.note < strings[1]: #between low E and A, add to E string...
				tab[5] += (str)(msg.note - strings[0])
				if(msg.note - strings[0]) > 9:
					tab[5] += "-"
			elif msg.note < strings[2]: #add to A
				tab[4] += (str)(msg.note - strings[1])
				if(msg.note - strings[1]) > 9:
					tab[4] += "-"
			elif msg.note < strings[3]: #add to D
				tab[3] += (str)(msg.note - strings[2])
				if(msg.note - strings[2]) > 9:
					tab[3] += "-"
			elif msg.note < strings[4]: #add to G
				tab[2] += (str)(msg.note - strings[3])
				if(msg.note - strings[3]) > 9:
					tab[2] += "-"
			elif msg.note < strings[5]: #below fret 0 of high E, add to B
				tab[1] += (str)(msg.note - strings[4])
				if(msg.note - strings[4]) > 9:
					tab[1] += "-"
			elif msg.note < strings[5] + numFrets: #below highest fret of hi E
				tab[0] += (str)(msg.note - strings[5])
				if(msg.note - strings[5]) > 9:
					tab[0] += "-"
			else:
				#print(msg)
				#print('message too high to add to tab')
				track_bad_flag = True
			#TODO add padding based on Time of msg compared to time of msg#n-1
			lengthen_empty_lines(tab)
	
	#for i, track...
	if not track_bad_flag:
		with open("{}_{}.txt".format(midi_source_file, track.name), 'w') as f:
			for line in tab:
				f.write(line)
				f.write('\n')
				#TODO wrap lines 6 at a time


#-----------------------------------------------------------------------
# things to do later maybe:

# create graph of possible tab-notes to find the "best" tab
# where best means "fewest hand-position changes"

# if a previous note's "note_off" is Later than the next note_on, add a ~
# to show that the note rings out
