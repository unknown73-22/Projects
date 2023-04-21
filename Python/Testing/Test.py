import tkinter as tk
import os

# Create a Tk object for the app window
root = tk.Tk()

# Get the width and height of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# Print the screen resolution
print(f"Screen resolution: {screen_width} x {screen_height}")

# Close the app window
root.destroy()
