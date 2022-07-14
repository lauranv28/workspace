# (x,y) -> (1,0) (-2,4)

suma = (1, 2) + (-2, 3) # -> (-1, 5)
resta = (1, 2) - (-2, 3) # -> (3, -1)
#Si hago print me concatena las tuplas, yo quiero que sume y reste

class Punto:
    #self hace referencia a la instancia (obj) en particular
    #__init__ guarda la información, tiene que ejecutarse si o sí
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, otro_punto): #Por defecto sabe que es sumar y no concatenar
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)
    def __sub__(self, otro): #El menos es un menos
        return Punto(self.x - otro.x, self.y - otro.y)
    def __str__(self):
        return f'({self.x}, {self.y})'
    def norma(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def distancia(self, otro_punto):
        return (self - otro_punto).norma()

primer_punto = Punto(1, 2)
segundo_punto = Punto(3, 4)

nuevo_punto_s = primer_punto + segundo_punto
nuevo_punto_r = primer_punto - segundo_punto
print(primer_punto.ditancia(segundo_punto))