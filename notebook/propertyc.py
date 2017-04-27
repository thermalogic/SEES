class CC:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
    
    x = property(getx, setx, delx, "I'm the 'x' property.")