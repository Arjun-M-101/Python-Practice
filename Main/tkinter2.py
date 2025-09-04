import tkinter as tk  # import the tkinter module

# Step 1: Create the main window
root = tk.Tk()
root.title("My First GUI")  # Set window title
root.geometry("300x200")  # Set width x height

tk.Label(root, text="Enter 1st number").pack(pady=5)
num1_entry = tk.Entry(root)
num1_entry.pack()

tk.Label(root, text="Enter 2nd number").pack(pady=5)
num2_entry = tk.Entry(root)
num2_entry.pack()

result_label = tk.Label(root, text="Result will appear here")
result_label.pack(pady=10)

def add_numbers():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num1_entry.get())
        total = num1 + num2
        result_label.config(text=f"Result is: {total}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

button = tk.Button(root, text="Calculate", command=add_numbers)
button.pack()

# Step 4: Start the GUI loop
root.mainloop()