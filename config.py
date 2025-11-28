"""
Configuration file for Pipes Falling app
Modify these values to customize the behavior
"""

# path to the sound file
SOUND_FILE = "metal pipe falling.mp3"

# how often to check if the sound should play (in seconds)
# default: 60 seconds
CHECK_INTERVAL = 60

# probability of playing the sound each check (0.0 to 1.0)
# default: 0.01 (1% chance)
# examples:
#   0.01 = 1% chance each check
#   0.05 = 5% chance each check
#   0.1 = 10% chance each check
CHANCE = 0.01

