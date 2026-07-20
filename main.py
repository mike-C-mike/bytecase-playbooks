"""ByteCase Playbooks entry point."""
import tkinter as tk

from gui import PlaybooksApp


def main():
    root = tk.Tk()
    PlaybooksApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
