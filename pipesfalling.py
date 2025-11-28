import sys
import random
import threading
import time
from pathlib import Path

import pystray
from PIL import Image
import pygame

try:
    from config import SOUND_FILE, CHECK_INTERVAL, CHANCE
except ImportError:
    SOUND_FILE = "metal pipe falling.mp3"
    CHECK_INTERVAL = 60
    CHANCE = 0.01


class PipesFallingApp:
    def __init__(self, sound_file="metal pipe falling.mp3", check_interval=60, chance=0.01):
        self.sound_file = sound_file
        self.check_interval = check_interval
        self.chance = chance
        self.running = False
        self.timer_thread = None
        
        pygame.mixer.init()
        
        self.icon = self.create_icon()
        
        self.menu = pystray.Menu(
            pystray.MenuItem("Status: Active", self.toggle_status, checked=lambda item: self.running),
            pystray.MenuItem("Test Sound", self.test_sound),
            pystray.MenuItem("Quit", self.quit_app)
        )
        
        self.tray_icon = pystray.Icon("Pipes Falling", self.icon, "Pipes Falling", self.menu)
    
    def create_icon(self):
        return Image.open("metalpipe.png")
    
    def play_sound(self):
        sound_path = Path(self.sound_file)
        if not sound_path.exists():
            print(f"Warning: Sound file '{self.sound_file}' not found!")
            return
        
        try:
            pygame.mixer.music.load(str(sound_path))
            pygame.mixer.music.play()
            print(f"Playing pipes falling sound at {time.strftime('%H:%M:%S')}")
        except pygame.error as e:
            print(f"Error loading/playing sound file: {e}")
        except Exception as e:
            print(f"Error playing sound: {e}")
    
    def test_sound(self, icon=None, item=None):
        self.play_sound()
    
    def check_and_play(self):
        # main loop that checks if sound should play
        while self.running:
            time.sleep(self.check_interval)
            if self.running and random.random() < self.chance:
                self.play_sound()
    
    def toggle_status(self, icon=None, item=None):
        # toggle the app on/off
        self.running = not self.running
        if self.running:
            if self.timer_thread is None or not self.timer_thread.is_alive():
                self.timer_thread = threading.Thread(target=self.check_and_play, daemon=True)
                self.timer_thread.start()
            print("Pipes Falling activated!")
        else:
            print("Pipes Falling deactivated!")
    
    def quit_app(self, icon=None, item=None):
        self.running = False
        self.tray_icon.stop()
        pygame.mixer.quit()
        sys.exit(0)
    
    def run(self):
        # start the app
        self.running = True
        self.timer_thread = threading.Thread(target=self.check_and_play, daemon=True)
        self.timer_thread.start()
        
        print("Pipes Falling is running in the system tray!")
        print("Right-click the tray icon to access the menu.")
        
        self.tray_icon.run()


def main():
    app = PipesFallingApp(
        sound_file=SOUND_FILE,
        check_interval=CHECK_INTERVAL,
        chance=CHANCE
    )
    app.run()


if __name__ == "__main__":
    main()

