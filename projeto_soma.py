#valor1, valor2, soma: real
#início
#Escreva "Digite o valor1"
#leia valor1
#Escreva "Digite o valor2"
#Leia valor2
#soma = valor1 + valor2
#Escreva "a soma é," soma
print("Programa somador!")

valor1 = float(input("Por favor, informe o primeiro valor: "))
valor2 = float(input("Por favor, informe o segundo valor: "))

soma = int(valor1) + int(valor2)

print("a soma é: {}".format(soma))
print(f"A soma é {soma}")