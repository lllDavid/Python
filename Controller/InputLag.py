import pygame
import time
import tkinter as tk
from tkinter import ttk

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

# Set up tkinter GUI
root = tk.Tk()
root.title("Gamepad Input Lag Display")

# Create a treeview to display button and axis lag
columns = ("Input", "Input Type", "Input Lag (seconds)")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Input", text="Input")
tree.heading("Input Type", text="Input Type")
tree.heading("Input Lag (seconds)", text="Input Lag (seconds)")
tree.pack(fill=tk.BOTH, expand=True)

# Dictionary to store lag information
lag_info = {}

# Function to update the treeview with lag information
def update_treeview():
    for input_name, info in lag_info.items():
        if input_name not in tree.get_children():
            tree.insert("", tk.END, iid=input_name, values=(input_name, info["type"], f"{info['lag']:.6f}"))
        else:
            tree.item(input_name, values=(input_name, info["type"], f"{info['lag']:.6f}"))
    root.after(100, update_treeview)

# Function to handle Pygame events and calculate input lag
def handle_events():
    global lag_info
    frame_start_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            root.quit()

        input_name = ""
        input_type = ""
        if event.type == pygame.JOYBUTTONDOWN:
            input_name = f"Button {event.button}"
            input_type = "Button Press"
        elif event.type == pygame.JOYBUTTONUP:
            input_name = f"Button {event.button}"
            input_type = "Button Release"
        elif event.type == pygame.JOYAXISMOTION:
            input_name = f"Axis {event.axis}"
            input_type = "Axis Motion"

        if input_name:
            event_time = time.time()
            input_lag = event_time - frame_start_time
            lag_info[input_name] = {"type": input_type, "lag": input_lag}

    root.after(10, handle_events)

# Start handling events and updating the GUI
handle_events()
update_treeview()

# Run the tkinter main loop
root.mainloop()

# Quit Pygame when done
pygame.quit()
