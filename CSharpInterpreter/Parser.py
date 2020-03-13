class Parser(object):

    lines: []
    classes: []

    result: str
    actualFileName: str

    def __init__(self):

        self.lines = []
        self.classes = []
        self.result = ""
        self.actualFileName = ""
        pass

    def Parse(self, fileName: str):

        self.actualFileName = fileName
        file = open(self.actualFileName)

        for line in file:
            self.lines.append(line)

        self.PrintFile()
        self.FindClasses()
        pass

    def FindClasses(self):

        classes = []

        for i in self.lines:
            line: str = i
            wordStart = line.find("class")

            if (wordStart != -1):

                startIndex, endIndex = self.FindWord(line, wordStart + len("class"))

                if (startIndex != -1):
                    className = line[startIndex:endIndex]
                    tmpClass = type(className)
                    classes.append(tmpClass)
                    print("Found class: " +  className)

                pass

        if (len(classes) == 0):
            print("No classes found in " + self.actualFileName)
        else:
            print(str(type(classes[0])))

        pass

    def FindWord(self, line: str, startIndex: int):

        iterator = startIndex;

        wordStart = -1;
        wordEnd = -1;

        while (startIndex != len(line)):

            if (wordStart == -1):
                if (line[iterator] != " " or line[iterator] != "\t"):
                    wordStart = iterator
                    pass
            else:
                if (iterator == len(line)):
                    wordEnd = iterator - 1
                    break

                if (line[iterator] == " " or line[iterator] == "\t"):
                    wordEnd = iterator - 1
                    break
            iterator += 1
            pass
        print ("Class indices start: " + str(wordStart) + " end: " + str(wordEnd))

        return (wordStart, wordEnd)

        pass

    def PrintFile(self):

        print("Lines count: ", len(self.lines))

        concatStr = ""

        for i in self.lines:
            concatStr += i

        print(concatStr)
        pass
