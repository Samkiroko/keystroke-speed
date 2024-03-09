import tkinter as tk
from tkinter import simpledialog
from pynput import keyboard
import time

# Global variables to store keystrokes and timing
start_time = None
keystroke_count = 0

def on_press(key):
    global start_time, keystroke_count
    if start_time is None:
        start_time = time.time()
    keystroke_count += 1

def calculate_speed(end_time):
    global start_time, keystroke_count
    elapsed_time = end_time - start_time
    speed = keystroke_count / elapsed_time * 60  # Keystrokes per minute (KPM)
    return speed, keystroke_count

def on_closing():
    global start_time, keystroke_count
    if start_time is not None:
        end_time = time.time()
        speed, total_strokes = calculate_speed(end_time)
        analysis = f"Keystroke Speed: {speed:.2f} KPM\nTotal Keystrokes: {total_strokes}"
        
        # Save the analysis to a text file
        with open('typing_analysis.txt', 'w') as file:
            file.write(analysis)
        
        print(analysis)
    root.destroy()

def main():
    global root
    root = tk.Tk()
    root.title("Typing Speed Application")
    
    tk.Label(root, text="Start typing in the box below. Close the window when done.").pack()
    text_widget = tk.Text(root, height=10, width=50)
    text_widget.pack()
    
    # Start listening to keystrokes
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    
    # Stop listening when the window is closed
    listener.stop()

if __name__ == "__main__":
    main()
