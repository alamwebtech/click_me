import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def say_hi():
	print("HELLO FROM PYTHON..!!")

button = tk.Button(frame, 
	                text="HIT ME",
	                fg="blue",
	                command=say_hi)

button.pack(side=tk.LEFT)
root.mainloop()
