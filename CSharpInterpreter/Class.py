



class Class(object):

    lines: []
    attributes: []

    def __init__(self, lines: []):
        self.lines = lines
        self._FindAttributes()
        self._FindMethods()
        pass

    def _FindAttributes(self):

        for i in self.lines:
            line: str = i

            if (line.find("private") != -1):

            






        pass
    pass

    def IsMethod(self, line: str):

        pass