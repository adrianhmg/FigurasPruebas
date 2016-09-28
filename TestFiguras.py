import unittest 
from figuras import Figuras

class TestFiguras(unittest.TestCase):
    
    def setUp(self):
        self.figura = Figuras()

    def test_area_cuadrado_lado_5(self):
        resultado = self.figura.cuadrado(5)
        self.assertEqual(25, resultado)
        
    def test_area_cuadrado_lado_6(self):
        resultado = self.figura.cuadrado(6)
        self.assertEqual(36, resultado)
        
    def test_area_cuadrado_lado_g(self):
        resultado = self.figura.cuadrado('g')
        self.assertEqual('Dato Incorrecto', resultado)
        
    def test_area_cuadrado_lado_decimal(self):
        resultado = self.figura.cuadrado(4.5)
        self.assertEqual(20.25, resultado)
    
    def test_area_rectangulo_lados_5_6(self):
        resultado = self.figura.rectangulo(5,6)
        self.assertEqual(30, resultado)
        
    def test_area_rectangulo_lados_8_4(self):
        resultado = self.figura.rectangulo(8,4)
        self.assertEqual(32, resultado)
        
    def test_area_rectangulo_lados_a_b(self):
        resultado = self.figura.rectangulo('a','b')
        self.assertEqual('Datos Incorrectos', resultado)
        
    def test_area_rectangulo_lados_decimal(self):
        resultado = self.figura.rectangulo(3.2,7.4)
        self.assertEqual(23.68, resultado)
    
    def test_area_triangulo_lados_4_3(self):
        resultado = self.figura.triangulo(4,3)
        self.assertEqual(6, resultado)
        
    def test_area_triangulo_lados_6_6(self):
        resultado = self.figura.triangulo(6,6)
        self.assertEqual(18, resultado)
        
    def test_area_triangulo_lados_b_a(self):
        resultado = self.figura.triangulo('b','a')
        self.assertEqual('Datos Incorrectos', resultado)
        
    def test_area_triangulo_lados_decimal(self):
        resultado = self.figura.triangulo(3.6,8.7)
        self.assertEqual(15.66, resultado)
        
    def test_area_circulo_radio_6(self):
        resultado = self.figura.circulo(6)
        self.assertEqual(113.1, resultado)
    
    def test_area_circulo_radio_2(self):
        resultado = self.figura.circulo(2)
        self.assertEqual(12.57, resultado)
    
    def test_area_circulo_radio_r(self):
        resultado = self.figura.circulo('r')
        self.assertEqual('Dato Incorrecto', resultado)
        
    def test_area_circulo_radio_decimal(self):
        resultado = self.figura.circulo(3.5)
        self.assertEqual(38.48, resultado)
        
    def tearDown(Self):
        pass
        
if __name__ == '__main__':
    unittest.main()