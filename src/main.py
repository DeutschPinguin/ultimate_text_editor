from tkinter import Tk, ttk
import menu, hotkeys


def main ():
    root = Tk()
    root.title('==- ULTIMATE TEXT EDITOR 2000 -==')
    
    menu.init(root)
    hotkeys.init(root)

    root.mainloop()


if __name__ == "__main__":
    main()