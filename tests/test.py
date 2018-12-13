import unittest
from app import Calculadora


class PruebaCalc(unittest.TestCase):
    def test_suma(self):
        c = Calculadora(2, 3)
        self.assertEqual(c.suma(), "La Suma de 2+3 es igual a 5")

    def test_suma_float(self):
        c = Calculadora(2.5, 2.5)
        self.assertEqual(c.suma(), "La Suma de 2.5+2.5 es igual a 5.0")

    def test_suma_N1(self):
        c = Calculadora(-2, 3)
        self.assertEqual(c.suma(), "La Suma de -2+3 es igual a 1")

    def test_suma_N2(self):
        c = Calculadora(2, -3)
        self.assertEqual(c.suma(), "La Suma de 2-3 (2+-3) es igual a -1")

    def test_suma_N1_N2(self):
        c = Calculadora(-2, -3)
        self.assertEqual(c.suma(), "La Suma de -2-3 (-2+-3) es igual a -5")

    def test_resta(self):
        c = Calculadora(5, 3)
        self.assertEqual(c.resta(), "La Resta de 5-3 es igual a 2")

    def test_resta_float(self):
        c = Calculadora(5.0, 2.5)
        self.assertEqual(c.resta(), "La Resta de 5.0-2.5 es igual a 2.5")

    def test_resta_N1(self):
        c = Calculadora(-5, 3)
        self.assertEqual(c.resta(), "La Resta de -5-3 es igual a -8")

    def test_resta_N2(self):
        c = Calculadora(5, -3)
        self.assertEqual(c.resta(), "La Resta de 5+3 (5--3) es igual a 8")

    def test_resta_N1_N2(self):
        c = Calculadora(-5, -3)
        self.assertEqual(c.resta(), "La Resta de -5+3 (-5--3) es igual a -2")

    def test_multiplicacion(self):
        c = Calculadora(5, 5)
        self.assertEqual(c.multiplicacion(), "La Multiplicacion de 5*5 es igual a 25")

    def test_multiplicacion_float(self):
        c = Calculadora(100.0, 0.5)
        self.assertEqual(c.multiplicacion(), "La Multiplicacion de 100.0*0.5 es igual a 50.0")

    def test_multiplicacion_float_0_N2(self):
        c = Calculadora(0.0, -2.0)
        self.assertEqual(c.multiplicacion(), "La Multiplicacion de 0.0*-2.0 es igual a 0.0")

    def test_multiplicacion_N1_N2(self):
        c = Calculadora(-5, -2)
        self.assertEqual(c.multiplicacion(), "La Multiplicacion de -5*-2 es igual a 10")

    def test_multiplicacion_N1(self):
        c = Calculadora(-5, 5)
        self.assertEqual(c.multiplicacion(), "La Multiplicacion de -5*5 es igual a -25")

    def test_multiplicacion_N2(self):
        c = Calculadora(7, -5)
        self.assertEqual(c.multiplicacion(), "La Multiplicacion de 7*-5 es igual a -35")

    def test_division(self):
        c = Calculadora(25, 5)
        self.assertEqual(c.division(), "La Division de 25/5 es igual a 5.0")

    def test_division_float(self):
        c = Calculadora(33.0, 5.5)
        self.assertEqual(c.division(), "La Division de 33.0/5.5 es igual a 6.0")

    def test_division_float_0_N2(self):
        c = Calculadora(0.0, -2.0)
        self.assertEqual(c.division(), "La Division de 0.0/-2.0 es igual a 0.0")

    def test_division_N1_N2(self):
        c = Calculadora(-10, -2)
        self.assertEqual(c.division(), "La Division de -10/-2 es igual a 5.0")

    def test_division_N1(self):
        c = Calculadora(-10, 2)
        self.assertEqual(c.division(), "La Division de -10/2 es igual a -5.0")

    def test_division_N2(self):
        c = Calculadora(30, -10)
        self.assertRegex(c.division(), "La Division de 30/-10 es igual a -3")
        # self.assertEqual(c.division(), "La Division de 30/-10 es igual a -3.0")

    def test_division_n20(self):
        c = Calculadora(100, 0)
        self.assertEqual(c.division(), "No se pueden realizar divisiones entre cero (100/0)")

    def test_division_n20(self):
        c = Calculadora(0, 10)
        self.assertEqual(c.division(), "La Division de 0/10 es igual a 0.0")

    def test_division_N20(self):
        c = Calculadora(0, -10)
        self.assertEqual(c.division(), "La Division de 0/-10 es igual a 0.0")

    def test_potencia(self):
        c = Calculadora(5, 2)
        self.assertEqual(c.potencia(), "La Potencia de 5^2 es igual a 25")
    def test_potencia_float(self):
        c = Calculadora(5.0, 2.0)
        self.assertEqual(c.potencia(), "La Potencia de 5.0^2.0 es igual a 25.0")

    def test_potencia_N1par(self):
        c = Calculadora(-2, 2)
        self.assertEqual(c.potencia(), "La Potencia de -2^2 es igual a 4")

    def test_potencia_N1impar(self):
        c = Calculadora(-2, 3)
        self.assertEqual(c.potencia(), "La Potencia de -2^3 es igual a -8")

    def test_potencia_N2(self):
        c = Calculadora(2, -2)
        self.assertEqual(c.potencia(), "El resultado de la potencia negativa 2^-2 es  1/4 o 0.25")

    def test_potencia_0(self):
        c = Calculadora(35, 0)
        self.assertEqual(c.potencia(), "Todo numero elevado a la 0 es igual a 1 (35^0)")

    def test_raiz_cuadrada(self):
        c = Calculadora(25, 2)
        self.assertEqual(c.raiz(), "La Raiz de 2√25 es igual a 5.0")

    def test_raiz_cuadrada_float(self):
        c = Calculadora(25.0, 2.0)
        self.assertEqual(c.raiz(), "La Raiz de 2.0√25.0 es igual a 5.0")

    def test_raiz_cubica(self):
        c = Calculadora(125, 3)
        self.assertEqual(c.raiz(), "La Raiz de 3√125 es igual a 5.0")

    def test_raiz_cubica_float(self):
        c = Calculadora(125.0, 3.0)
        self.assertEqual(c.raiz(), "La Raiz de 3.0√125.0 es igual a 5.0")

    def test_raiz_N1par(self):
        c = Calculadora(-25, 2)
        self.assertEqual(c.raiz(), "No se pueden realizar raices pares de numeros negativos (2√-25)")

    def test_raiz_N1inpar(self):
        c = Calculadora(-125, 3)
        self.assertEqual(c.raiz(), "La Raiz impar (3) del numero negativo -125 (3√-125) es igual a -5.0")

    def test_raiz_N2par(self):
        c = Calculadora(25, -2)
        self.assertEqual(c.raiz(), "La Raiz negativa de -2√25 es igual a 1/5.0 o 0.2")

    def test_raiz_N2inpar(self):
        c = Calculadora(125, -3)
        self.assertEqual(c.raiz(), "La Raiz negativa de -3√125 es igual a 1/5.0 o 0.2")

    def test_raiz_n20(self):
        c = Calculadora(125, 0)
        self.assertEqual(c.raiz(), "No se pueden realizar raices a la 0 (0√125)")

    def test_raiz_n10(self):
        c = Calculadora(0, 2)
        self.assertEqual(c.raiz(), "La Raiz de 2√0 es igual a 0.0")
