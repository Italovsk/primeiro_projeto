#importação do módulo calc.py
from calc import *
#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma
soma = somar(valor1,valor2)
subtracao = subtrair(valor1,valor2)
divisao = dividir(valor1,valor2)
#exibindo a soma
print("A soma é {}".format(soma))
print(f"A subtração é {subtracao}")
print(f"A divisão é {divisao}")
