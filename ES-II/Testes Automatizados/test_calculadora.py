#Author: Gabrielli Danker 
#Editado: 24/05/2024

import math
import unittest

class Calculadora:
    def adicao(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida \n")
        return a / b
    
    def exponenciacao(self, a, b):
        return a ** b
    
    def raiz_quadrada(self, a):
        if a < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo \n")
        return math.sqrt(a)

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        # Estado Inicial: Calculadora instanciada.
        self.calc = Calculadora()
    def test_adicao(self):
        # Entradas de teste: (1, 2), (-1, -1), (0, 0)
        # Condições de execução: Chamar o método adicao com as entradas fornecidas
        # Saídas esperadas: 3, -2, 0
        print("\nTeste de Adição")
        resultado = self.calc.adicao(1, 2)
        print(f"1 + 2 = {resultado}")
        self.assertEqual(resultado, 3)
        
        resultado = self.calc.adicao(-1, -1)
        print(f"-1 + -1 = {resultado}")
        self.assertEqual(resultado, -2)
        
        resultado = self.calc.adicao(0, 0)
        print(f"0 + 0 = {resultado}")
        self.assertEqual(resultado, 0)   
        
    def test_subtracao(self):
        # Entradas de teste: (5, 3), (0, 0), (-1, -1)
        # Condições de execução: Chamar o método subtracao com as entradas fornecidas
        # Saídas esperadas: 2, 0, 0
        print("\nTeste de Subtração")
        resultado = self.calc.subtracao(5, 3)
        print(f"5 - 3 = {resultado}")
        self.assertEqual(resultado, 2)
        
        resultado = self.calc.subtracao(0, 0)
        print(f"0 - 0 = {resultado}")
        self.assertEqual(resultado, 0)
        
        resultado = self.calc.subtracao(-1, -1)
        print(f"-1 - -1 = {resultado}")
        self.assertEqual(resultado, 0)
    
    def test_multiplicacao(self):
        # Entradas de teste: (2, 3), (-1, -1), (0, 5)
        # Condições de execução: Chamar o método multiplicacao com as entradas fornecidas
        # Saídas esperadas: 6, 1, 0
        print("\nTeste de Multiplicação")
        resultado = self.calc.multiplicacao(2, 3)
        print(f"2 * 3 = {resultado}")
        self.assertEqual(resultado, 6)
        
        resultado = self.calc.multiplicacao(-1, -1)
        print(f"-1 * -1 = {resultado}")
        self.assertEqual(resultado, 1)
        
        resultado = self.calc.multiplicacao(0, 5)
        print(f"0 * 5 = {resultado}")
        self.assertEqual(resultado, 0)
    
    def test_divisao(self):
        # Entradas de teste: (6, 3), (1, 0), (-4, 2)
        # Condições de execução: Chamar o método divisao com as entradas fornecidas
        # Saídas esperadas: 2, ValueError, -2
        print("\nTeste de Divisão")
        resultado = self.calc.divisao(6, 3)
        print(f"6 / 3 = {resultado}")
        self.assertEqual(resultado, 2)
        
        print("1 / 0 = Error esperado")
        with self.assertRaises(ValueError):
            self.calc.divisao(1, 0)
        
        resultado = self.calc.divisao(-4, 2)
        print(f"-4 / 2 = {resultado}")
        self.assertEqual(resultado, -2)
    
    def test_exponenciacao(self):
        # Entradas de teste: (2, 3), (5, 0), (-1, 2)
        # Condições de execução: Chamar o método exponenciacao com as entradas fornecidas
        # Saídas esperadas: 8, 1, 1
        print("\nTeste de Exponenciação")
        resultado = self.calc.exponenciacao(2, 3)
        print(f"2 ^ 3 = {resultado}")
        self.assertEqual(resultado, 8)
        
        resultado = self.calc.exponenciacao(5, 0)
        print(f"5 ^ 0 = {resultado}")
        self.assertEqual(resultado, 1)
        
        resultado = self.calc.exponenciacao(-1, 2)
        print(f"-1 ^ 2 = {resultado}")
        self.assertEqual(resultado, 1)
    
    def test_raiz_quadrada(self):
        # Entradas de teste: (4), (0), (-1)
        # Condições de execução: Chamar o método raiz_quadrada com as entradas fornecidas
        # Saídas esperadas: 2, 0, ValueError
        print("\nTeste de Raiz Quadrada")
        resultado = self.calc.raiz_quadrada(4)
        print(f"sqrt(4) = {resultado}")
        self.assertEqual(resultado, 2)
        
        resultado = self.calc.raiz_quadrada(0)
        print(f"sqrt(0) = {resultado}")
        self.assertEqual(resultado, 0)
        
        print("sqrt(-1) = Error esperado")
        with self.assertRaises(ValueError):
            self.calc.raiz_quadrada(-1)

if __name__ == '__main__':
    unittest.main()
