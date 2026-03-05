from tkinter import Tk, ttk


def addTo (root: Tk):
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Button(frame, text='Quit', command=root.destroy).grid(column=1, row=0)
