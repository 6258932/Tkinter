
import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

label1 = tk.Label(root, text="Label 1")
label1.place(x=1, y=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=1, column=1)


squareA = tk.Canvas(root, bg="red")
squareA.grid(row=0, column=0)

squareB = tk.Canvas(root, bg="blue")
squareB.grid(row=0, column=1)

root.mainloop()
