# midi_to_tab
converts midi files to readable guitar tablature

dependencies:
- python
- mido: https://pypi.org/project/mido/

usage:
# python midiToTab.py <PathToYourMidiFile>.mid

what it does:
reads the provided midi file and, for every track that contains 1 or more notes, if all of those notes can be played on a guitar in standard tuning, creates a .txt file that contains a valid (though probably not optimal) tab for that track.
the txt file will be named `MidiFile_TrackName.txt`.

why is it non-optimal? or in other words, what am i going to implement if i keep working on this?
- it doesnt contain measure breaks
- it doesnt account for alternate tunings or different numbers of strings or frets (unless you modify those variables in the script)
- it prefers to play every note in its left-most possible position instead of a natural hand position which considers its context.

if you want the tab to be good, consider using tuttut, a more complete version of this same idea: https://github.com/natecdr/tuttut
