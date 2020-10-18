import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.filedialog
import pinyin as pin
import function
import pinyin_modules
import re

vocab_list = []
index = 0
filename = ""
random_order = []


def file_read():
    global vocab_list
    fTyp = [("", "*")]
    iDir = './imported_csv'
    # ファイル選択ダイアログの表示
    filename = tkinter.filedialog.askopenfilename(
        filetypes=fTyp, initialdir=iDir)
    filename = re.search('\/imported_csv\/.*', filename)
    filename = re.sub('\/imported_csv\/', '', filename.group())
    filename = re.sub('\.csv', '', filename)
    vocab_list, random_order = function.csv_shuffle_read(filename)


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("640x360")
        self.resizable(0, 0)
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
        # 初期化
        global vocab_list, index

        vocab_list = []
        index = 0

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
            command=lambda: master.switch_frame(SetChar)
        ).grid(row=0, column=1)
        ttk.Label(
            self,
            text='勉強をはじめる',
            font=('Helvetica', 18),
            relief="groove"
        ).grid(row=1, column=0)
        ttk.Label(
            self,
            text='単語帳を作る',
            font=('Helvetica', 18),
            relief="groove"
        ).grid(row=1, column=1)


class PagePrp(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)

        tk.Button(self, text="単語帳を選ぶ", font=('Helvetica', 18),
                  command=lambda: file_read()).grid(row=0, column=0)
        ttk.Button(self, text="Go to Next", command=lambda: master.switch_frame(
            PageAns)).grid(row=1, column=0)
        ttk.Button(self, text="Go back to start page", command=lambda: master.switch_frame(
            StartPage)).grid(row=2, column=0, pady=10)


class PageAns(tk.Frame):
    def __init__(self, master):
        global index
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)

        if(index == len(vocab_list)):
            ret = tk.messagebox.showinfo("お疲れさまでした", "終了しました")

            if ret == ok:
                master.switch_frame(StartPage)
        ttk.Label(self, text="漢字").grid(row=0, column=0)
        ttk.Label(self, text="拼音").grid(row=1, column=0)
        ttk.Label(self, text="和訳").grid(row=2, column=0)


        kanji = tk.StringVar()
        pinyin = tk.StringVar()
        mean = tk.StringVar()

        kanji.set(' ')
        pinyin.set(' ')
        mean.set(' ')

        LabelK = ttk.Label(
            self, text=kanji.get()).grid(row=0, column=1)
        LabelP = ttk.Label(
            self, text=pinyin.get()).grid(row=1, column=1)
        LabelM = ttk.Label(
            self, text=mean.get()).grid(row=2, column=1)

        def keycall1(event):
            show_kanji()
        def keycall2(event):
            show_pinyin()
        def keycall3(event):
            show_pinyin()

        def show_kanji():
            kanji.set(vocab_list[index][0])
            LabelK = ttk.Label(self, text=kanji.get())
            LabelK.grid(row=0, column=1)
        def show_pinyin():
            pinyin.set(vocab_list[index][1])
            LabelP = ttk.Label(self, text=pinyin.get())
            LabelP.grid(row=1, column=1)
        def show_mean():
            mean.set(vocab_list[index][2])
            LabelM = ttk.Label(self, text=mean.get())
            LabelM.grid(row=2, column=1)

        def next_vocab():
            global index
            index += 1
            master.switch_frame(PageAns)

        ttk.Button(self, text="OPEN", command=lambda: show_kanji()
                   ).grid(row=0, column=2)
        ttk.Button(self, text="OPEN", command=lambda: show_pinyin()
                   ).grid(row=1, column=2)
        ttk.Button(self, text="OPEN", command=lambda: show_mean()
                   ).grid(row=2, column=2)

        # self.bind("<Z>", keycall1)
        # self.bind("<X>", keycall2)
        # self.bind("<C>", keycall3)

        ttk.Button(self, text="Next", command=lambda: next_vocab()
                   ).grid(row=3, column=2)
        ttk.Button(self, text="Go back to start page", command=lambda: master.switch_frame(
            StartPage)).grid(row=4, column=0, columnspan=self.grid_size()[0], pady=10)

        col_count, row_count = self.grid_size()

        for col in range(col_count):
            self.grid_columnconfigure(col, minsize=100)

        for row in range(row_count):
            self.grid_rowconfigure(row, minsize=40)


class SetChar(tk.Frame):
    def __init__(self, master):
        global index
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)
        ttk.Label(self, text="単語帳制作", font=(
            'Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=2)
        ttk.Label(self, text="漢字を入力してください", font=(
            'Helvetica', 18, "bold")).grid(row=1, column=0, columnspan=2)

        var = tk.StringVar()

        def next_vocab():
            global index
            vocab_list.append([])
            vocab_list[index].append(var.get())
            index += 1
            master.switch_frame(SetChar)

        def move_to_pinyin():
            global index
            vocab_list.append([])
            vocab_list[index].append(var.get())
            index = 0
            master.switch_frame(CheckPinyin)

        ttk.Entry(self, textvariable=var,
                  width=20).grid(row=2, column=0, pady=10, columnspan=2)
        ttk.Button(self, text="次の単語",
                   command=lambda: next_vocab()).grid(row=3, column=0)
        ttk.Button(self, text="漢字登録完了",
                   command=lambda: move_to_pinyin()).grid(row=3, column=1)
        ttk.Button(self, text="Go back to start page", command=lambda: master.switch_frame(
            StartPage)).grid(row=4, column=0, columnspan=2, pady=10)


class CheckPinyin(tk.Frame):
    def __init__(self, master):
        global vocab_list, index
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)
        num_pinyin = pin.get(vocab_list[index][0], format='numerical')
        pinyin = pinyin_modules.no_num_pinyin(num_pinyin)
        var = tk.StringVar()
        var.set(num_pinyin)

        ttk.Label(self, text="単語帳制作", font=(
            'Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=2)
        ttk.Label(self, text="拼音が間違っていれば修正してください", font=(
            'Helvetica', 18, "bold")).grid(row=1, column=0, columnspan=2)
        ttk.Label(self, text=vocab_list[index][0] + ': ' + pinyin, font=(
            'Helvetica', 18, "bold")).grid(row=2, column=0, columnspan=2)

        def next_vocab():
            global index
            vocab_list[index].append(var.get())
            index += 1
            master.switch_frame(CheckPinyin)

        def move_to_pinyin():
            global index
            vocab_list[index].append(var.get())
            index = 0
            master.switch_frame(InputMeaning)
        if index > len(vocab_list):
            move_to_pinyin()
        ttk.Entry(self, textvariable=var,
            width=20).grid(row=3, column=0, columnspan=2)
        ttk.Button(self, text="修正不要", command=lambda: next_vocab()
            ).grid(row=4, column=0)
        ttk.Button(self, text="修正したい", command=lambda: move_to_pinyin()
            ).grid(row=4, column=1)
        ttk.Button(self, text="Go back to start page", command=lambda: master.switch_frame(
            StartPage)).grid(row=5, column=0, columnspan=2)


class InputMeaning(tk.Frame):
    def __init__(self, master):
        global index
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)

        var = tk.StringVar()

        ttk.Label(self, text="単語帳制作", font=(
            'Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=2)
        ttk.Label(self, text="和訳を入力してください", font=(
            'Helvetica', 18, "bold")).grid(row=1, column=0, columnspan=2)
        ttk.Label(self, text=vocab_list[index][0] + ': ' + pinyin, font=(
            'Helvetica', 18, "bold")).grid(row=2, column=0, columnspan=2)

        def next_vocab():
            global index
            vocab_list[index].append(var.get())
            index += 1
            master.switch_frame(InputMeaning)
        def save_and_move_to_start():
            global index
            vocab_list[index].append(var.get())
            index = 0
            master.switch_frame(InputFinish)
        if index > len(vocab_list):
            save_and_move_to_start()
        ttk.Entry(self, textvariable=var,
            width=20).grid(row=1, column=1, pady=10, columnspan=2)
        ttk.Button(self, text="OK", command=lambda: next_vocab()
            ).grid(row=4, column=1)
        ttk.Button(self, text="修正したい", command=lambda: save_and_move_to_start()
            ).grid(row=4, column=3)
        ttk.Button(self, text="Go back to start page", command=lambda: master.switch_frame(
            StartPage)).grid(row=4, column=2, columnspan=2, pady=10)

class InputFinish(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        ttk.Frame.configure(self)

        ttk.Label(self, text="入力終了！お疲れ様でした！", font=(
            'Helvetica', 18, "bold")).grid(row=0, column=0, columnspan=2)

        ttk.Button(self, text="Go back to start page", command=lambda: master.switch_frame(
            StartPage)).grid(row=4, column=2, columnspan=2, pady=10)


if __name__ == "__main__":
    app = SampleApp()
    app.grid_anchor(tk.CENTER)
    app.mainloop()
