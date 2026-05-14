import math

# Point Class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __repr__(self):
        return f"({self.x}, {self.y})"



# Cross Product / Orientation Test

def cross(O, A, B): 
    return ((A.x - O.x) * (B.y - O.y)
          - (A.y - O.y) * (B.x - O.x))



# Euclidean Distance
def distance(A, B):
    return math.sqrt((A.x - B.x) ** 2 +
                     (A.y - B.y) ** 2)
