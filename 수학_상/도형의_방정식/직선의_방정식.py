import math 

def 두_점으로_기울기(한_점, 다른_점):
    return (한_점.y - 다른_점.y) / (한_점.x - 다른_점.x)

class 직선:
    def __init__(self, 기울기=None, x절편=None, y절편=None, 한_점=None, 다른_점=None, a=None, b=None, c=0):
        if 기울기:
            self.m = 기울기
            if y절편 is not None: # 기울기 m과 y절편 n이 주어진 경우 
                self.n = y절편
            else: # 기울기 m과 한 점이 주어진 경우
                self.n = 한_점.y - (self.m * 한_점.x)
            self.a, self.b, self.c = self.m, -1, self.n
        elif 한_점 and 다른_점: # 두 점이 주어진 경우 
            self.m = 두_점으로_기울기(한_점, 다른_점)
            self.n = 한_점.y - (self.m * 한_점.x)
            self.a, self.b, self.c = self.m, -1, self.n
        else: # 직선의 일반형이 주어진 경우 
            self.a, self.b, self.c = a, b, c
            self.m = - (self.a / self.b)
            self.n = - (self.c / self.b)
    
    def __repr__(self):
        return '<직선 %s>' % self.기본형()

    def 기본형(self):
        s = 'y='
        if (self.m):
            if (self.m == 1):
                s += 'x'
            elif (self.m == -1):
                s += '-x'
            else:
                s += '%sx' % str(int(self.m))
        if (self.n):
            if (self.n > 0):
                s += '+'
            s += '%s' % str(int(self.n))
        if s == 'y=':
            s += '0'
        return s
    
    def 표준형(self):
        return 

    def 일반형(self):
        return 
    
    def 한_점에서_만남(self, l):
        return (self.m != l.m)
    
    def 일치(self, l):
        return (self.m == l.m) and (self.n == l.n)

    def 평행(self, l):
        return (self.m == l.m) and (self.n != l.n)

    def 직교(self, l):
        return (self.m * l.m) == -1

    def 대입(self, x, y):
        return self.a * x + self.b * y + self.c
    
    def 점과의_거리(self, 한_점):
        분자 = abs(self.대입(한_점.x, 한_점.y))
        분모 = math.sqrt(self.a ** 2 + self.b ** 2)
        return 분자 / 분모
    
    def 평행이동(self, p=0, q=0):
        return 직선(
            a = self.a,
            b = self.b,
            c = - (self.a * p + self.b * q - self.c)
        )
    
    def 점대칭이동(self, p):
        pass
    
    def 선대칭이동(self, l):
        pass
