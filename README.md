# keyboardsoundmakerthing
A simple Python program that plays mechanical keyboard sounds when keys are pressed. The program features a graphical user interface (GUI) with options to toggle the sound on and off, select different keyboard sounds, and adjust the volume.
## Features

- Toggle sound on/off with a button.
- Select different mechanical keyboard sounds from a dropdown menu.
- Adjust sound volume with a slider.
- Prevents sound spamming by implementing a cooldown period between key presses.

## Requirements

- Python 3.x
- `pygame` library
- `pynput` library
- `tkinter` (included with Python)

## Installation

1. Ensure you have Python 3 installed. If not, download and install it from [python.org](https://www.python.org/).

2. Install the required libraries using pip:
    ```sh
    pip install pygame pynput
    ```

3. Download or clone this repository.

4. Place your sound files (e.g., `mechanical1.wav`, `mechanical2.wav`, `mechanical3.wav`) in the same directory as the script. Right now I have only included `keyboard.mp3`, script will work fine with that file.

## Usage

1. Run the script:
    ```sh
    python kb.py
    ```

2. A GUI window will open with the following options:
    - **Toggle Sound**: Turns the sound on or off.
    - **Sound Selection**: Choose different mechanical keyboard sounds from the dropdown menu.
    - **Volume Control**: Adjust the sound volume using the slider.

3. When the sound is on, pressing any key on your keyboard will play the selected sound with the specified volume.

## Code Overview

### Main Components

- **play_sound()**: Plays the selected sound if the cooldown period has passed.
- **on_press(key)**: Handles key press events and calls `play_sound()` if the sound is toggled on.
- **toggle_sound()**: Toggles the sound on and off.
- **select_sound(event)**: Updates the current sound based on the user's selection.
- **set_volume(val)**: Adjusts the sound volume based on the slider value.

### GUI Elements

- **Toggle Button**: A button to toggle the sound on and off.
- **Status Label**: Displays the current sound status (ON/OFF).
- **Sound Dropdown**: A dropdown menu to select different mechanical keyboard sounds.
- **Volume Slider**: A slider to adjust the volume of the sound.
