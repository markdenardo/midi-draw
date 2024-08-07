from PIL import Image, ImageDraw
from midiutil import MIDIFile

# Load and analyze the image
image = Image.open('/Users/mdn/Desktop/python-projects/AUG/midi-draw/images/test.png')
width, height = image.size

# Create MIDIFile object
midi = MIDIFile(numTracks=4, adjust_origin=True)

# Track settings
track = 0
time = 0
channel = 0  # Example: map different channels to different line thicknesses

# Analyze the image and map lines to MIDI notes
for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        # Example: check if pixel represents a line of certain thickness
        if pixel == (0, 0, 0):  # Assuming line is black
            # Example: determine pitch based on y position
            pitch = 60 + int((y / height) * 20)  # Example pitch mapping
            # Example: determine duration based on x position
            duration = int((x / width) * 2)  # Example duration mapping
            # Example: add note to MIDI track
            midi.addNote(track, channel, pitch, time, duration, 100)

# Write MIDI file to disk
with open('output.mid', 'wb') as f:
    midi.writeFile(f)
