import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Point(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

def plane_angle(a, b, c, d):
    AB = b - a
    AC = c - a

    BC = c - b
    BD = d - b
    
    #нормали плоскостей
    X = AB.cross(AC)
    Y = BC.cross(BD)
    
    #от деления на ноль
    len_x = X.absolute()
    len_y = Y.absolute()
    
    if len_x == 0 or len_y == 0:
        return 0.0
    
    cos_phi = X.dot(Y) / (len_x * len_y)
    cos_phi = max(-1.0, min(1.0, cos_phi))
    
    #острый угол
    phi_rad = math.acos(abs(cos_phi))
    
    return math.degrees(phi_rad)