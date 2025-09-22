#Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada. Para isso, você deve solicitar que o usuário informe o seu número de BATIMENTOS POR MINUTO(BPM) e a IDADE. A partir disso o script deve verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada.

#IDADE BPM
#ATÉ 2 ANOS 120 A 140
#De 8 até 17 anos 80 a 100
#Adulto sedentário 70 a 80
#Idosos de 50 a 60
print("VERIFICADOR DE FREQUÊNCIA CARDÍACA")
idade = int(input("Por favor digite sua idade: "))
bpm = int(input("Por favor informe seu idade: "))

if idade <= 2:
    if bpm >= 120:
        if bpm <= 140:
            print("Batimentos normais para a idade fornecida")
        else:
            print("Batimentos acima dos indicados para a idade")
    else:
        print("Batimentos abaixo dos indicados para a idade")
elif idade >= 8:
    if idade <= 17:
        if bpm >= 80:
            if bpm <= 100:
                print("Batimentos normais para a idade fornecida")
            else:
                print("Batimentos acima para a idade fornecida")
        else:
            print("Batimentos abaixo para a idade fornecida")
    if idade >= 18:
        if idade <= 60:
            if bpm >= 70:
                if bpm <= 80:
                    print("Batimentos normais para a idade fornecida")
                else:
                    print("Batimentos acima para a idade fornecida")
            else:
                print("Batimentos abaixo para a idade fornecida")
        else:
            if bpm >= 50:
                if bpm <= 60:
                    print("Batimentos normais para a idade fornecida")
                else:
                    print("Batimentos acima para a idade fornecida")
            else:
                print("Batimentos abaixo para a idade fornecida")
else:
    print("Não foi possível verificar os batimentos para esta idade")