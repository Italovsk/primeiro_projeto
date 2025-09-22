#Pedir a distancia da viagem
distancia = float(input("Por favor digite a distância percorrida: "))
#Pedir o tempo da viagem
tempo = float(input("Por favor informe o tempo necessário para a viagem: "))
#Dividir a distancia pelo tempo
velocidade_media = distancia / tempo
#Exibir o resultado para o usuário
print("A velocidade média foi de {:.2f} km/h".format(velocidade_media))
print(f"A velocidade média foi de {velocidade_media:.2f} km/h")