class Triangulo:
    def __init__ (self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimetro (self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return "equilátero"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isósceles"
        else:
            return "escaleno"
    def retangulo(self):
        return ((self.a**2 == self.b ** 2 + self.c**2)
        or (self.b**2 == self.a**2 + self.c**2)
        or (self.c**2 == self.a**2 + self.b**2))
    def semelhantes(self, t2):
        ''' semelhança de triangulo'''
        return (self.a/t2.a == self.b/t2.b == self.c/t2.c)
