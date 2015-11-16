class Widget():
    def __init__(self, name,size = (40, 40)):
        self._name=name
        self._size =size

    def name(self):
        return self._name

    def size(self):
        return self._size

    def resize(self, width, height):
        if width < 0  or height < 0:
            raise(ValueError, "illegal size")
        self._size = (width, height)

    def dispose(self):
        pass
