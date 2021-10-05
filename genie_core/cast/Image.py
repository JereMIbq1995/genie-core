from .trait import Trait

class Image(Trait):
    def __init__(self, path : str = "", 
                    scale : float = 1,
                    rotation : float = 0):
        self._path = path
        self._scale = scale
        self._rotation = rotation
    
    def get_path(self):
        return self._path
    
    def set_path(self, path : str):
        self._path = path
    
    def get_scale(self):
        return self._scale
    
    def set_scale(self, scale : float):
        self._scale = scale
    
    def get_rotation(self):
        return self._rotation
    
    def set_rotation(self, rotation : float):
        self._rotation = rotation