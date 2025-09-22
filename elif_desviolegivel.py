pontuação = int(input("Por favor informa pontuação do usuário: "))

if pontuação >= 1000:
    print("Você recebeu 3gb de bônus")
elif pontuação >= 500:
    print("Você recebeu 1,5gb de bônus")
elif pontuação >= 200:
    print("Você recebeu 500mb de bônus")
else:
    print("Você não tem pontuação suficiente para resgatar o bônus")

