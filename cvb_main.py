import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.filedialog


def file_read():

    fTyp = [("", "*")]
    iDir = './imported_csv'
    # ファイル選択ダイアログの表示
    file_path = tkinter.filedialog.askopenfilename(
        filetypes=fTyp, initialdir=iDir)

    if len(file_path) != 0:
        # ファイルが選択された場合

        # ファイルを開いて読み込んでdataに格納
        f = open(file_path)
        data = f.read()
        f.close()
    else:
        # ファイル選択がキャンセルされた場合

        # dataは空にする
        data = ''

    return data


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


def showSome(i):
    i += 1
    if i >= 3:
        ttk.Label(self, text=kanji).grid(row=0, column=1)
        ttk.Label(self, text=pinyin).grid(row=1, column=1)
        ttk.Label(self, text=mean).grid(row=2, column=1)
    elif i >= 2:
        ttk.Label(self, text=kanji).grid(row=0, column=1)
        ttk.Label(self, text=pinyin).grid(row=1, column=1)
    else:
        ttk.Label(self, text=kanji).grid(row=0, column=1)

    return i


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
            command=lambda: master.switch_frame(PagePrp)
        ).grid(row=0, column=0)
        ttk.Button(
            self,
            image=self.icon2,
            command=lambda: master.switch_frame(PageMak)
        ).grid(row=0, column=1)
        ttk.Label(
            self,
            text='勉強をはじめる'
        ).grid(row=1, column=0)
        ttk.Label(
            self,
            text='単語帳を作る'
        ).grid(row=1, column=1)


class PagePrp(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)
        ttk.Button(self, text="単語帳データを選ぶ",
                   command=lambda: file_read()).grid(row=0, column=0)
        ttk.Button(self, text="Go to Next", command=lambda: master.switch_frame(
            PageAns)).grid(row=0, column=1)


class PageAns(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)
        ttk.Label(self, text="漢字").grid(row=0, column=0)
        ttk.Label(self, text="拼音").grid(row=1, column=0)
        ttk.Label(self, text="和訳").grid(row=2, column=0)

        kanji = "あああ"
        pinyin = "ボタンを押してスタート"
        mean = "あああ"

        ttk.Button(self, text="Next", command=lambda: ).grid(row=1, column=2)


class PageMak(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)
        ttk.Label(self, text="Page two", font=(
            'Helvetica', 18, "bold")).grid(row=0, column=0)
        ttk.Button(self, text="Go back to start page", command=lambda: master.switch_frame(
            StartPage)).grid(row=0, column=1)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
