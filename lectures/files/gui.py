import tkinter

root = tkinter.Tk()
text = tkinter.Text(root, height=20, width=100)
text.pack()
text.insert(tkinter.END, "Line 1\nLine 2\n")
tkinter.mainloop()
