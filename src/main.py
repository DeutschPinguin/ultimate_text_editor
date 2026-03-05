from tkinter import Tk, ttk
import tkinter, files, menu, hotkeys, texteditor


def main ():
    root = Tk()
    root.title('==- ULTIMATE TEXT EDITOR 2000 -==')
    
    fr = ttk.Frame(root, padding=(3, 3, 12, 12))
    fr.grid(column=0, row=0, sticky='nwes')

    files.init(root)
    menu.init(root)
    hotkeys.init(root)
    texteditor.init(root)

    root.mainloop()


if __name__ == "__main__":
    main()