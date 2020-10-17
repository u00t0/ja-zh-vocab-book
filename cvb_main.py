import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("640x360")
        self.title("Test")
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


class StartPage(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        img1 = Image.open('learn.png')
        img2 = Image.open('make.png')

        self.icon1 = ImageTk.PhotoImage(img1)
        self.icon2 = ImageTk.PhotoImage(img2)

        ttk.Button(
            self,
            image=self.icon1,
            command=lambda: master.switch_frame(PageOne)
        ).grid(row=0, column=0)
        ttk.Button(
            self,
            image=self.icon2,
            command=lambda: master.switch_frame(PageOne)
        ).grid(row=0, column=1)
        ttk.Label(
            self,
            text='勉強をはじめる'
        ).grid(row=1, column=0)
        ttk.Label(
            self,
            text='単語帳を作る'
        ).grid(row=1, column=1)


class PageOne(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)
        ttk.Label(self, text="Page one", font=(
            'Helvetica', 18, "bold")).grid(row=0, column=0)
        ttk.Button(self, text="Go back to start page",
                   command=lambda: master.switch_frame(StartPage)).grid(row=0, column=1)


class PageTwo(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)
        ttk.Label(self, text="Page two", font=(
            'Helvetica', 18, "bold")).grid(row=0, column=0)
        ttk.Button(self, text="Go back to start page",
                   command=lambda: master.switch_frame(StartPage)).grid(row=0, column=1)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
