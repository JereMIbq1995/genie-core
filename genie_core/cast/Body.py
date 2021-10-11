from .trait import Trait

class Body(Trait):
    def __init__(self, x : float = 0, 
                    y : float = 0,
                    vx : float = 0,
                    vy : float = 0,
                    height : float = 0, 
                    width : float = 0):
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy
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
    
    def incr_x(self, dx):
        self._x += dx
    
    def incr_y(self, dy):
        self._y += dy
    
    def move(self):
        """
            Move the object if the velocities are > 0
        """
        self._x += self._vx
        self._y += self._vy