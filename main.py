import tkinter as tk
from pynput import keyboard
import time

# Global variables to store keystrokes, timing, and text input
start_time = None
keystroke_count = 0
text_input = ""
keystrokes_log_path = 'keystrokes_log.txt'

def on_press(key):
    global keystroke_count
    keystroke_count += 1
    with open(keystrokes_log_path, 'a') as log_file:
        try:
            # Log alphanumeric keys
            log_file.write(f'Alphanumeric key pressed: {key.char}\n')
        except AttributeError:
            # Log special keys
            if key == keyboard.Key.space:
                log_file.write('Space\n')
            elif key == keyboard.Key.enter:
                log_file.write('Enter\n')
            elif key == keyboard.Key.backspace:
                log_file.write('Backspace\n')
            elif key == keyboard.Key.cmd:
                log_file.write('Command\n')
            elif key == keyboard.Key.ctrl:
                log_file.write('Control\n')
            else:
                log_file.write(f'Special key pressed: {key}\n')

def calculate_speed(end_time):
    global start_time, keystroke_count
    elapsed_time = end_time - start_time
    speed = keystroke_count / elapsed_time * 60  # Keystrokes per minute (KPM)
    return speed, keystroke_count

def on_closing():
    global start_time, keystroke_count, text_input
    if start_time is not None:
        end_time = time.time()
        speed, total_strokes = calculate_speed(end_time)
        text_input = text_widget.get("1.0", tk.END).strip()  # Get text from widget
        analysis = f"Typed Text: {text_input}\nKeystroke Speed: {speed:.2f} KPM\nTotal Keystrokes: {total_strokes}"
        
        # Save the analysis to a text file
        with open('typing_analysis.txt', 'w') as file:
            file.write(analysis + '\n')
        
        # Append the keystrokes log to the analysis file
        with open(keystrokes_log_path, 'r') as log_file, open('typing_analysis.txt', 'a') as analysis_file:
            analysis_file.write('\nKeystrokes Log:\n')
            analysis_file.write(log_file.read())
        
        print(analysis)
    root.destroy()

def main():
    global root, text_widget, start_time, duration
    # Clear previous keystrokes log
    open(keystrokes_log_path, 'w').close()
    
    # Input duration from the console
    duration = int(input("Enter the duration for typing in seconds: "))
    start_time = time.time()  # Initialize start time
    
    root = tk.Tk()
    root.title("Typing Speed Application")
    
    tk.Label(root, text="Start typing in the box below. The window will close automatically when the time is up.").pack()
    text_widget = tk.Text(root, height=10, width=50)
    text_widget.pack()
    
    # Schedule the window to close after the input duration
    root.after(duration * 1000, on_closing)
    
    # Start listening to keystrokes
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    
    # Stop listening when the window is closed
    listener.stop()

if __name__ == "__main__":
    main()
