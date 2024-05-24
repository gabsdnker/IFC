#Author: Gabrielli Danker 
#Editado: 24/05/2024

import math

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

def menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Exponenciação")
    print("6. Raiz Quadrada")
    print("7. Sair")
    escolha = input("Digite o número da operação desejada: ")
    return escolha

if __name__ == "__main__":
    calc = Calculadora()
    
    while True:
        opcao = menu()
        
        if opcao == '7':
            print("Obrigado por usar a calculadora. Até logo!")
            break
        
        if opcao in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Digite um número: "))
                if opcao != '6':
                    num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira números válidos.")
                continue
            
            if opcao == '1':
                print("Resultado:", calc.adicao(num1, num2), "\n")
            elif opcao == '2':
                print("Resultado:", calc.subtracao(num1, num2), "\n")
            elif opcao == '3':
                print("Resultado:", calc.multiplicacao(num1, num2), "\n")
            elif opcao == '4':
                try:
                    print("Resultado:", calc.divisao(num1, num2), "\n")
                except ValueError as e:
                    print(e)
            elif opcao == '5':
                print("Resultado:", calc.exponenciacao(num1, num2), "\n")
            elif opcao == '6':
                try:
                    print("Resultado:", calc.raiz_quadrada(num1), "\n")
                except ValueError as e:
                    print(e)
        else:
            print("Opção inválida. Por favor, escolha uma operação válida.")
