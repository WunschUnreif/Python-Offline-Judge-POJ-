import os
from POfJ_diff import *

class Problem:
    def __init__(self, probPath):
        self.probPath = probPath
        self.badProb = False
        self.hasDatagen = False
        self.hasStdprog = True
        self.openInfo()
        if not self.badProb:
            lines = self.probInfo.readlines()
            self.probName = lines[0][:-1]
            for i in range(1, 3):
                l = lines[i]
                if l[0] == 'd' and l[8] == 't':
                    self.hasDatagen = True
                if l[0] == 's' and l[8] == 'f':
                    self.hasStdprog = False
            self.probID = int(lines[3])
            self.probInfo.close()
            self.getProbDescribe()


    def openInfo(self):
        self.probInfo = None
        try:
            self.probInfo = open(self.probPath + 'probinfo', encoding='utf-8')
        except IOError as e:
            self.badProb = True

    def getProbDescribe(self):
        describe = open(self.probPath + 'probdescribe', encoding='utf-8')
        self.probDescribe = describe.read()
        describe.close()

    def genData(self):
        if self.hasDatagen == False:
            return
        os.system("python %sdatagen.py > %sstdinput" % (self.probPath, self.probPath))
        os.system("python %sstdprog.py < %sstdinput > %sstdoutput" % (self.probPath, self.probPath, self.probPath))

    def testUserCode(self, userCodePath):
        self.genData()
        os.system("python %s < %sstdinput > %suseroutput" %(userCodePath, self.probPath, self.probPath))
        ret = diff("%suseroutput" % self.probPath, "%sstdoutput" % self.probPath)
        return ret


if __name__ == '__main__':
    problem = Problem("../problems/Set01/Prob01/")
    print(problem.probName)
    print(problem.hasDatagen)
    print(problem.hasStdprog)
    print(problem.probID)
    print(problem.probDescribe)
    print(problem.testUserCode("../problems/Set01/Prob01/stdprog.py"))
