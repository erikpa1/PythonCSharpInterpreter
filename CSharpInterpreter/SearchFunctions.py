

def FindWord(line: str, startIndex: int):
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
    print("Class indices start: " + str(wordStart) + " end: " + str(wordEnd))

    return (wordStart, wordEnd)

    pass

    def FindCurveEnd(array: [], startIndex: int):

        leftCurves = 1;
        rightCurves = 0;


        for lineIndex in range(startIndex, len(startIndex)):

            line: str = array[lineIndex];

            leftCurves += line.count("{")
            rightCurves += line.count("}")

            if leftCurves == rightCurves:
                return lineIndex

            return -1
            pass

        pass
