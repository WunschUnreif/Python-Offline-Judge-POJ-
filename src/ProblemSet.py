import os
from Problem import Problem

problemSets = []

class ProblemSet:
    def __init__(self, setPath):
        self.setName = None
        self.setPath = setPath
        self.badset = False
        self.problems = []
        self.problemNumber = 0
        self.openInfo()
        if not self.badset:
            self.setName = self.setInfo.readlines()[0][:-1]
            fileList = os.listdir(setPath)
            for name in fileList:
                if os.path.isdir(os.path.join(setPath, name)):
                    if(name[0:4] == 'Prob'):
                        self.problems.append(Problem(os.path.join(setPath, name) + '\\'))
            self.problemNumber = len(self.problems)

    def openInfo(self):
        self.setInfo = None
        try:
            self.setInfo = open(self.setPath + 'setinfo', encoding='utf-8')
        except IOError as e:
            self.badset = True



def getProblemSets():
    names = os.listdir("../problems")
    for name in names:
        if os.path.isdir(os.path.join("../problems", name)) and name[0:3] == 'Set':
            problemSets.append(ProblemSet(os.path.join("../problems", name) + '\\'))

getProblemSets()

# if __name__ == '__main__':
#     getProblemSets()
#     for ps in problemSets:
#         print(ps.setName)
#         for p in ps.problems:
#             print("|---%s\n" % p.probName)
#             print(p.probDescribe)
