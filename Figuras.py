import math

class Figuras:
    
    def cuadrado(self, lado):
        try:
            lado = float(lado)
            return lado * lado
        except Exception, e:
            return 'Dato Incorrecto'
            
    def rectangulo(self, ladoUno, ladoDos):
        try:
            ladoUno = float(ladoUno)
            ladoDos = float(ladoDos)
            area = ladoUno * ladoDos
            return float("%.2f" % area)
        except Exception, e:
            return'Datos Incorrectos'
            
    def triangulo(self, base, altura):
        try:
            base = float(base)
            altura = float(altura)
            area = (base * altura)/2
            return float("%.2f" % area)
        except Exception, e:
            return 'Datos Incorrectos'
            
    def circulo(self, radio):
        try:
            radio = float(radio)
            pi = 3.1416
            area = pi * (radio**2)
            return float("%.2f" % area)
        except Exception, e:
            return 'Dato Incorrecto'
            
            
            