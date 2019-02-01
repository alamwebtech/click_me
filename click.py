import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


	

button = tk.Button(frame, 
	                text="HIT ME",
	                fg="blue",
	                command=lambda: print(print("HELLO FROM PYTHON..!!"))

button.pack(side=tk.LEFT)
root.mainloop()

