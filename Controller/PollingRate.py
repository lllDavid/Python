import pygame
import tkinter as tk
from tkinter import ttk
import time

# Initialize Pygame and the joystick
pygame.init()
pygame.joystick.init()

# Detect if any gamepad is connected
if pygame.joystick.get_count() == 0:
    print("No gamepad detected.")
    pygame.quit()
    exit()

# Initialize the first gamepad
gamepad = pygame.joystick.Joystick(0)
gamepad.init()
print(f"Gamepad initialized: {gamepad.get_name()}")

# Create GUI with Tkinter
root = tk.Tk()
root.title("Gamepad Stats")

# Create labels to display controller statistics
status_label = tk.Label(root, text="Polling Rate: Calculating...")
status_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

axis_frame = tk.Frame(root)
axis_frame.pack(pady=10)

# Create dictionaries to store button and axis stats
button_labels = {}
axis_labels = {}

def update_controller_stats():
    global button_labels, axis_labels
    # Poll Pygame events
    events = pygame.event.get()
    
    # Update controller statistics
    num_buttons = gamepad.get_numbuttons()
    num_axes = gamepad.get_numaxes()
    
    # Update button states
    for i in range(num_buttons):
        button_state = gamepad.get_button(i)
        if i not in button_labels:
            button_labels[i] = tk.Label(button_frame, text=f"Button {i}: {button_state}")
            button_labels[i].pack()
        else:
            button_labels[i].config(text=f"Button {i}: {button_state}")

    # Update axis states
    for i in range(num_axes):
        axis_value = gamepad.get_axis(i)
        if i not in axis_labels:
            axis_labels[i] = tk.Label(axis_frame, text=f"Axis {i}: {axis_value:.2f}")
            axis_labels[i].pack()
        else:
            axis_labels[i].config(text=f"Axis {i}: {axis_value:.2f}")

    # Update polling rate
    current_time = time.time()
    polling_rate = 1 / (current_time - update_controller_stats.last_call_time) if update_controller_stats.last_call_time else 0
    update_controller_stats.last_call_time = current_time
    status_label.config(text=f"Polling Rate: {polling_rate:.2f} Hz")
    
    # Schedule the next update
    root.after(100, update_controller_stats)

# Initialize the last call time for polling rate calculation
update_controller_stats.last_call_time = time.time()

# Start updating the GUI with controller stats
update_controller_stats()

# Run the tkinter main loop
root.mainloop()

# Quit Pygame when done
pygame.quit()
