import math

class 점:
    def __init__(self, x=0, y=0, 이름=None):
        self.x, self.y = x, y
        self.이름 = 이름

    def __repr__(self):
        if self.이름:
            return '<점 %s(%d, %d)>' % (self.이름, self.x, self.y)
        return '<점 (%d, %d)>' % (self.x, self.y)
    
    def 점과의_거리(self, 한_점):
        return math.sqrt(
            (self.x - 한_점.x) ** 2 +
            (self.y - 한_점.y) ** 2
        )

    def 직선과의_거리(self, 한_직선):
        return 한_직선.점과의_거리(self)

    def 선분과의_거리(self, 한_선분):
        return 

class 선분:
    def __init__(self):
        pass

class 삼각형:
    def __init__(self):
        pass

    def __repr__(self):
        return '<삼각형>'
