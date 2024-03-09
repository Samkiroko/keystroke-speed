import tkinter as tk
from tkinter import simpledialog
from pynput import keyboard
import time

# Global variables to store keystrokes, timing, and text input
start_time = None
keystroke_count = 0
text_input = ""

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
    global start_time, keystroke_count, text_input
    if start_time is not None:
        end_time = time.time()
        speed, total_strokes = calculate_speed(end_time)
        text_input = text_widget.get("1.0", tk.END).strip()  # Get text from widget
        analysis = f"Typed Text: {text_input}\nKeystroke Speed: {speed:.2f} KPM\nTotal Keystrokes: {total_strokes}"
        
        # Save the analysis to a text file
        with open('typing_analysis.txt', 'w') as file:
            file.write(analysis)
        
        print(analysis)
    root.destroy()

def auto_close():
    root.after(duration * 1000, on_closing)  # Close window after duration

def main():
    global root, text_widget, duration
    root = tk.Tk()
    root.title("Typing Speed Application")
    
    # Ask for duration input
    duration = simpledialog.askinteger("Duration", "Enter the duration for typing in seconds:")
    
    tk.Label(root, text="Start typing in the box below. The window will close automatically when the time is up.").pack()
    text_widget = tk.Text(root, height=10, width=50)
    text_widget.pack()
    
    # Start listening to keystrokes
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    auto_close()  # Schedule the window to close after the input duration
    
    root.mainloop()
    
    # Stop listening when the window is closed
    listener.stop()

if __name__ == "__main__":
    main()
