import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import ProblemSet as ps
import tkinter.messagebox
import POfJ_diff as diff

class POJ_App:
    def __init__(self):
        self.probSet = ps.problemSets
        self.root = tk.Tk()
        self.root.title("Python Offline Judge(POJ)")
        #self.root.geometry('655x480')
        self.mainframe = ttk.Frame(self.root).grid(column=0, row=0, sticky='news')
        self.notebook = ttk.Notebook(self.mainframe)
        self.notebook.grid(column=0, row=0, sticky='news')
        self.drawViewChooseProblem()
        self.drawViewBrowseProblem()
        self.drawViewJudge()
        #self.addMenus()
        self.root.mainloop()

    def addMenus(self):
        self.menubar = ttk.Menubutton(self.mainframe, text='帮助')
        self.menubar.grid(column=0, row=0, sticky='W')

    def listProbSet(self):
        self.showingPSet = True
        cnt = 0
        self.probListBox.delete(0, tk.END)
        for p in self.probSet:
            cnt += 1
            self.probListBox.insert(tk.END, "问题集1%03d    |    %s"%(cnt, p.setName))

    def listProblem(self):
        if not self.showingPSet:
            tk.messagebox.showerror("我好像不太明白。。。", "你选的这个似乎不是一个问题集\n试试中间那个按钮吧^_^")
            return
        pSel = self.probListBox.curselection()
        if not pSel:
            tk.messagebox.showerror("我好像不太明白。。。", "你似乎并没有选择任何问题集^_^")
            return
        self.pset = self.probSet[pSel[0]];
        self.probListBox.delete(0, tk.END)
        for p in self.pset.problems:
            self.probListBox.insert(tk.END, "问题%s    |    %s"%(p.probID,p.probName))
        self.showingPSet = False

    def chooseProblem(self):
        if self.showingPSet:
            tk.messagebox.showerror("我好像不太明白。。。", "你选的这个似乎不是一个问题\n试试右边那个按钮吧^_^")
            return
        pSel = self.probListBox.curselection()
        if not pSel:
            tk.messagebox.showerror("我好像不太明白。。。", "你似乎并没有选择任何问题^_^")
            return
        self.problem = self.pset.problems[pSel[0]]
        self.notebook.select(1)
        self.showProbDescription(self.problem)
        #print(self.problem.probName)


    def drawViewChooseProblem(self):
        self.pset = None
        self.problem = None
        self.frameChooseProblem = ttk.Frame(self.notebook)

        ttk.Style().configure("A.TButton", font='宋体 -22 bold')

        self.frameChooseProblem.grid(column=0, row=0, sticky='news')
        self.btnConfirm = ttk.Button(self.frameChooseProblem, text='对，就是这道！', style="A.TButton", command=self.chooseProblem)
        self.btnConfirm.grid(column=2, row=10, columnspan=2, sticky=tk.NSEW, padx=24)
        self.btnEnter = ttk.Button(self.frameChooseProblem, text='进入这个问题集！', style="A.TButton", command=self.listProblem)
        self.btnEnter.grid(column=4, row=10, columnspan=2, sticky=tk.E)
        self.btnBack = ttk.Button(self.frameChooseProblem, text='返回问题集浏览界面', style="A.TButton", command=self.listProbSet)
        self.btnBack.grid(column=0, row=10, columnspan=2, sticky=tk.W)

        self.probListBox = tk.Listbox(self.frameChooseProblem, height=20, font="宋体 -17", selectmode=tk.SINGLE)
        probListScrollBar = ttk.Scrollbar(self.frameChooseProblem, orient=tk.VERTICAL)
        self.probListBox.grid(column=0, row=1, columnspan=6, sticky=tk.NSEW, pady=18)
        probListScrollBar.grid(column=6, row=1, sticky='ns')
        probListScrollBar.config(command=self.probListBox.yview)
        self.probListBox.config(yscrollcommand=probListScrollBar.set)
        self.listProbSet()

        self.notebook.add(self.frameChooseProblem, text='挑选题目')

    def drawViewJudge(self):
        self.programPath = None
        self.frameJudge = ttk.Frame(self.notebook)
        self.frameJudge.grid(column=0,row=0, sticky='news')

        #ttk.Style().configure("A.TButton", font='宋体 -22 bold')

        self.codeView = tk.Text(self.frameJudge, width=56, height=18, font='"Courier New" -18', state=tk.DISABLED)
        self.codeView.grid(column=0, row=0, columnspan=3, sticky='news', pady=20)

        btnOpenProg = ttk.Button(self.frameJudge, text='选择程序文件', style='A.TButton', command=self.chooseProgram)
        btnOpenProg.grid(column=0, row=1, sticky='news', padx=3)
        btnRunJudeg = ttk.Button(self.frameJudge, text='运行测评', style='A.TButton', command=self.runJudge)
        btnRunJudeg.grid(column=1, row=1, sticky='news', padx=3)
        btnCloseProb = ttk.Button(self.frameJudge, text='关闭问题', style='A.TButton', command=self.closeProblem)
        btnCloseProb.grid(column=2, row=1, sticky='news', padx=3)

        codeViewScrollBar = ttk.Scrollbar(self.frameJudge, orient=tk.VERTICAL)
        codeViewScrollBar.grid(column=3, row=0,sticky='ns')
        codeViewScrollBar.config(command=self.codeView.yview)
        self.codeView.config(yscrollcommand=codeViewScrollBar.set)

        self.notebook.add(self.frameJudge, text='程序评测')

    def chooseProgram(self):
        if self.problem is None:
            tk.messagebox.showerror("我好像不太明白。。。", "你好像还没有选择问题\n先去选一道题吧^_^")
            return
        path = askopenfilename(title='选择Python文件', initialdir="../../", filetypes=(("Python Source Code", "*.py"),))
        self.programPath = path
        if path:
            f = open(path, encoding='utf-8')
            code = f.read()
            self.codeView.config(state=tk.NORMAL)
            self.codeView.delete('0.0', tk.END)
            self.codeView.insert(tk.END, code)
            self.codeView.config(state=tk.DISABLED)

    def runJudge(self):
        if self.problem is None:
            tk.messagebox.showerror("我好像不太明白。。。", "你好像还没有选择问题\n先去选一道题吧^_^")
            return
        if self.programPath is None:
            tk.messagebox.showerror("我好像不太明白。。。", "你好像还没有选择程序\n试试左边的按钮吧^_^")
            return
        testResult = self.problem.testUserCode(self.programPath)
        if testResult == diff.ACCEPTED:
            tk.messagebox.showinfo("你成功了！！！", "你很出色地完成了题目\n\"%s\"\n继续前进吧！" % self.problem.probName)
        elif testResult == diff.WRONG_ANSWER:
            tk.messagebox.showinfo("糟糕。。。", "很遗憾，你的程序没有输出正确的结果。\n没关系，你还可以再试试^_^")


    def drawViewBrowseProblem(self):
        self.frameBrowseProblem = ttk.Frame(self.notebook)
        self.frameBrowseProblem.grid(column=0, row=0, sticky='news')

        self.probView = tk.Text(self.frameBrowseProblem, width=77, height=22, font=' -20', state=tk.DISABLED)
        self.probView.grid(column=0, row=0, columnspan=2, sticky='news', pady=20)

        btnEnterJudge = ttk.Button(self.frameBrowseProblem, text='进入评测界面', style='A.TButton', command=self.enterJudge)
        btnEnterJudge.grid(column=0, row=1, sticky='news', padx=3)
        btnCloseProb = ttk.Button(self.frameBrowseProblem, text='关闭问题', style='A.TButton', command=self.closeProblem)
        btnCloseProb.grid(column=1, row=1, sticky='news', padx=3)

        probViewScrollBar = ttk.Scrollbar(self.frameBrowseProblem, orient=tk.VERTICAL)
        probViewScrollBar.grid(column=2, row=0,sticky='ns')
        probViewScrollBar.config(command=self.probView.yview)
        self.probView.config(yscrollcommand=probViewScrollBar.set)

        self.notebook.add(self.frameBrowseProblem, text='浏览题目')

    def enterJudge(self):
        self.notebook.select(2)

    def showProbDescription(self, problem):
        self.probView.config(state=tk.NORMAL)
        self.probView.delete('0.0', tk.END)
        self.probView.insert(tk.END, problem.probDescribe)
        self.probView.config(state=tk.DISABLED)

    def closeProblem(self):
        self.problem = None
        self.programPath = None
        self.probView.config(state=tk.NORMAL)
        self.probView.delete('0.0', tk.END)
        self.probView.config(state=tk.DISABLED)
        self.codeView.config(state=tk.NORMAL)
        self.codeView.delete('0.0', tk.END)
        self.codeView.config(state=tk.DISABLED)
        self.notebook.select(0)

app = POJ_App()
