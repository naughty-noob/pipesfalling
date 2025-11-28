# pipesfalling

who dosent love it when pipes just randomly fall

A system tray app that randomly plays the pipes falling sound effect.

## Setup

1. Install the stuff:
   ```bash
   pip install -r requirements.txt
   ```

2. The sound file is already included (`metal pipe falling.mp3`), so you're good to go!

3. Run it:
   ```bash
   python pipesfalling.py
   ```

## How it works

- Checks every 60 seconds by default
- Has a 1% chance to play the sound each check
- Lives in your system tray
- Right-click the icon to test the sound or quit

## Customize it

Edit `config.py` if you want to change:
- `CHECK_INTERVAL` - how often it checks (in seconds)
- `CHANCE` - probability of playing (0.01 = 1%, 0.05 = 5%, etc.)

That's it. Enjoy the chaos.
