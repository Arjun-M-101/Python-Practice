import tkinter as tk  # import the tkinter module

# Step 1: Create the main window
root = tk.Tk()
root.title("My First GUI")  # Set window title
root.geometry("300x200")  # Set width x height

# Step 2: Add a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Add vertical padding

# Step 3: Add a button
def on_click():
    label.config(text="You clicked the button!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# Step 4: Start the GUI loop
root.mainloop()