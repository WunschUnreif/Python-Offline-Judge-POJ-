import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename

class POJ_App:
    def __init__(self):
        self.rootWindow = tk.Tk()
        self.rootWindow.title('Python Offline Judge(POJ)')
        self.rootWindow.geometry('1000x800')
        self.frame = ttk.Frame(self.rootWindow)
        self.frame.pack()
        self.makeNoteBook()
        self.rootWindow.mainloop()

    def makeNoteBook(self):
        self.noteBook = ttk.Notebook(self.frame, width=1000, height=600)
        self.noteBook.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        self.addTabChooseProblems()

    def addTabChooseProblems(self):
        self.frameChooseProb = ttk.Frame(self.noteBook, name='chooseProb')
        self.labelChooseProb = ttk.Label(self.frameChooseProb, text="选择一个问题集")
        self.labelChooseProb.pack()
        def hide():
            self.noteBook.hide(tab_id=0)
        btnHide = ttk.Button(self.frameChooseProb, text='HIDE', command=hide)
        btnHide.pack()
        self.noteBook.add(self.frameChooseProb, text="选择试题", sticky='w')

app = POJ_App()
