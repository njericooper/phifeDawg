## An example of how classes call upon each other


class P1:
    def __init__(self, side=1):
        self._side = side
class S1(P1):
    def x1(self, side):
        return side * side
class S2(P1):
    def x1 (self, side=2):
            return side * side * 5

a = S2()
print(a.x1(1))            
