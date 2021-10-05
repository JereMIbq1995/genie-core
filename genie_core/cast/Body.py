from .trait import Trait

class Body(Trait):
    def __init__(self, x : float = 0, 
                    y : float = 0, 
                    height : float = 0, 
                    width : float = 0):
        self._x = x
        self._y = y
        self._height = height
        self._width = width
    
    def get_position(self):
        return (self._x, self._y)
    
    def set_position(self, x : float, y : float):
        self._x = x
        self._y = y
    
    def get_height(self):
        return self._height
    
    def set_height(self, height : float):
        self._height = height
    
    def get_width(self):
        return self._width
    
    def set_width(self, width : float):
        self._width = width