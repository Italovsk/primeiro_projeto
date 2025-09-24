resposta = ""
tentativas = 0

while resposta != "42":
    resposta = input("Qual é a resposta da vida, o universo e tudo mais?")
    tentativas = tentativas + 1

print("Parabéns! Você acertou! \nNão esqueça a sua toalha!")
print(f"Você precisou de {tentativas} tentativas!")
