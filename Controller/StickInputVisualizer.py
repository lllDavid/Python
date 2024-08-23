import pygame
import tkinter as tk
from tkinter import Canvas

# Initialize Pygame
pygame.init()
pygame.joystick.init()

gamepad_count = pygame.joystick.get_count()
print(f"Number of Gamepads detected: {gamepad_count}")

# Initialize each gamepad
gamepads = []
for i in range(gamepad_count):
    gamepad = pygame.joystick.Joystick(i)
    gamepad.init()
    gamepads.append(gamepad)
    print(f"Gamepad {i} initialized: {gamepad.get_name()}")

# Global variables for axis positions and which stick to monitor
x, y = 0, 0
monitoring_left_stick = True

# Function to update the position of the dot and the axis values on the canvas
def update_gui():
    global x, y, monitoring_left_stick
    
    # Poll Pygame events
    events = pygame.event.get()

    left_stick_active = False
    right_stick_active = False
    
    for event in events:
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0 or event.axis == 1:
                left_stick_active = True
            elif event.axis == 2 or event.axis == 3:
                right_stick_active = True

    # Toggle between sticks based on input
    if left_stick_active and not monitoring_left_stick:
        monitoring_left_stick = True
        stick_label.config(text="Monitoring: Left Stick")
    elif right_stick_active and monitoring_left_stick:
        monitoring_left_stick = False
        stick_label.config(text="Monitoring: Right Stick")

    # Update position based on active stick
    for event in events:
        if event.type == pygame.JOYAXISMOTION:
            if monitoring_left_stick:
                if event.axis == 0:  # Left stick X-axis motion
                    x = event.value
                elif event.axis == 1:  # Left stick Y-axis motion
                    y = event.value
            else:
                if event.axis == 2:  # Right stick X-axis motion
                    x = event.value
                elif event.axis == 3:  # Right stick Y-axis motion
                    y = event.value

    # Update axis value labels
    x_label.config(text=f"X Axis: {x:.2f}")
    y_label.config(text=f"Y Axis: {y:.2f}")

    # Calculate the new position
    canvas.coords(dot, canvas_center_x + x * canvas_radius - dot_radius, 
                  canvas_center_y + y * canvas_radius - dot_radius, 
                  canvas_center_x + x * canvas_radius + dot_radius, 
                  canvas_center_y + y * canvas_radius + dot_radius)

    root.after(1, update_gui)

# Set up tkinter GUI
root = tk.Tk()
root.title("Gamepad Input Display")

canvas_width = 400
canvas_height = 400
canvas_center_x = canvas_width // 2
canvas_center_y = canvas_height // 2
canvas_radius = canvas_width // 2

canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Draw the cross axis
canvas.create_line(canvas_center_x, 0, canvas_center_x, canvas_height, fill="black")
canvas.create_line(0, canvas_center_y, canvas_width, canvas_center_y, fill="black")

# Create a dot to represent the gamepad's stick position
dot_radius = 5
dot = canvas.create_oval(canvas_center_x - dot_radius, canvas_center_y - dot_radius,
                         canvas_center_x + dot_radius, canvas_center_y + dot_radius,
                         fill="red")

# Label to show which stick is being monitored
stick_label = tk.Label(root, text="Monitoring: Left Stick")
stick_label.pack(pady=10)

# Labels to show X and Y axis values
x_label = tk.Label(root, text=f"X Axis: {x:.2f}")
x_label.pack(pady=5)

y_label = tk.Label(root, text=f"Y Axis: {y:.2f}")
y_label.pack(pady=5)

# Start updating the GUI with gamepad inputs
update_gui()

# Run the tkinter main loop
root.mainloop()

# Quit Pygame on exit
pygame.quit()
