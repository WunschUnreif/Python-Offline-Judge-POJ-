#This module provide a function to check whether if two files are the same.
#The function will ignore spaces at the end of line.
#And also the returns at the end of file.

#define constants.
FILE_NOT_FOUND = -1
FILE_FOUND = 2
WRONG_ANSWER = 1
ACCEPTED = 0

#two files.
userFile = None
standardFile = None

#this function may be called outside the module.
def diff(userOutFile, stdOutFile):
    return diffFile(userOutFile, stdOutFile)

#try to open files.
def openFile(userOutFile, stdOutFile):
    global userFile, standardFile

    #make sure those files aren't from last diff.
    userFile = None
    standardFile = None

    #initialize the return value.
    retValue = FILE_FOUND

    try:
        userFile = open(userOutFile)
        standardFile = open(stdOutFile)
    except IOError as e:
        retValue = FILE_NOT_FOUND #if the file cannot be opened.

    return retValue

def diffFile(userOutFile, stdOutFile):
    global userFile, standardFile

    #try to open files using function openFile.
    if openFile(userOutFile, stdOutFile) == FILE_NOT_FOUND:
        return FILE_NOT_FOUND;

    #get the list of lines fron the files.
    userLines = userFile.readlines()
    stdLines = standardFile.readlines()

    #diff the files and keep the return value.
    retValue = diffLines(userLines, stdLines)

    #make sure the files will be closed.
    #when program runs here, it's certain that the files have been opened,
    #so there is no need to check whether they're opened.
    userFile.close()
    standardFile.close()

    return retValue

def diffLines(userLines, stdLines):
    #declare two lists to store the standardnized lines.
    userLinesWithoutSpaces = []
    stdLinesWithoutSpaces = []

    #the following program will cut the spaces at the end of line.
    for line in userLines:
        cutPos = 0   #records where is the last nospace character.
        iterCnt = 0  #records the loop varible.
        for char in line:
            iterCnt += 1
            if char != ' ' and char != '\n' and char != '\r':
                cutPos = iterCnt #if we detected a nonspace, we assume it may be
                                 #the last nonspace.
        #and the following will cut the returns at the end of file.
        if cutPos == 0:
            continue
        #append the  standardnized line.
        userLinesWithoutSpaces.append(line[:cutPos])

    #this loop has the same function as above.
    for line in stdLines:
        cutPos = 0
        iterCnt = 0
        for char in line:
            iterCnt += 1
            if char != ' ' and char != '\n' and char != '\r':
                cutPos = iterCnt
        if cutPos == 0:
            continue
        stdLinesWithoutSpaces.append(line[:cutPos])

    userLines = userLinesWithoutSpaces
    stdLines = stdLinesWithoutSpaces

    #if the answers don't even have the same quantity of lines.
    if len(userLines) != len(stdLines):
        return WRONG_ANSWER
    #check line by line.
    for i in range(len(userLines)):
        if userLines[i] != stdLines[i]:
            return WRONG_ANSWER
    return ACCEPTED


# #test program.
# if __name__ == '__main__':
#     print(diff("a.txt", "b.txt"))
