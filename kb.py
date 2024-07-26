import tkinter as tk
from tkinter import ttk
import pygame
from pynput import keyboard
import time

# Initialize Pygame mixer for sound playback
pygame.mixer.init()

# Load sound files into a dictionary
sounds = {
    "Keyboard": 'keyboard.mp3',
}

# Default sound
current_sound = pygame.mixer.Sound(sounds["Keyboard"])

# Cooldown configuration
cooldown = 0.2  # in seconds
last_played_time = time.time()  # Initialize with the current time

# Function to play sound
def play_sound():
    global last_played_time
    current_time = time.time()
    if current_time - last_played_time >= cooldown:
        print("Playing sound")  # Debugging statement
        current_sound.play()
        last_played_time = current_time
    else:
        print("Cooldown in effect")  # Debugging statement

# Handler for key press
def on_press(key):
    if is_active:
        try:
            play_sound()
        except Exception as e:
            print(f"Error playing sound: {e}")  # Debugging statement

# Toggle button callback
def toggle_sound():
    global is_active
    is_active = not is_active
    status_label.config(text="Sound: ON" if is_active else "Sound: OFF")

# Sound selection callback
def select_sound(event):
    global current_sound
    sound_name = sound_var.get()
    current_sound = pygame.mixer.Sound(sounds[sound_name])
    print(f"Selected sound: {sound_name}")  # Debugging statement

# Volume control callback
def set_volume(val):
    volume = float(val) / 100
    current_sound.set_volume(volume)
    print(f"Set volume to: {volume}")  # Debugging statement

# Initial setup
is_active = False
root = tk.Tk()
root.title("Keyboard Sound Selector")

# Toggle button
toggle_button = tk.Button(root, text="Toggle Sound", command=toggle_sound)
toggle_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text="Sound: OFF")
status_label.pack(pady=10)

# Sound selection dropdown
sound_var = tk.StringVar(value="Keyboard")
sound_dropdown = ttk.Combobox(root, textvariable=sound_var, values=list(sounds.keys()))
sound_dropdown.bind("<<ComboboxSelected>>", select_sound)
sound_dropdown.pack(pady=10)

# Volume slider
volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume", command=set_volume)
volume_slider.set(100)
volume_slider.pack(pady=10)

# Keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Run the GUI
root.mainloop()