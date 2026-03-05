from tkinter import Tk, ttk
import tkinter, files, menu, hotkeys, texteditor


def main ():
    root = Tk()
    root.title('==- ULTIMATE TEXT EDITOR 2000 -==')
    
    fr = ttk.Frame(root, padding=(3, 3, 12, 12))
    fr.grid(column=0, row=0, sticky='nwes')
    root.geometry(newGeometry="720x640+" + str(int(root.winfo_screenwidth() / 4)) + "+" + str(int(root.winfo_screenheight() / 4)))

    files.init(root)
    menu.init(root)
    hotkeys.init(root)
    texteditor.init(root)

    root.mainloop()


if __name__ == "__main__":
    main()