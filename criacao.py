def velocidade_media(distancia, tempo):
    vm = distancia / tempo
    return vm

velocidades_medias = []
for dia in ["segunda", "terça", "quarta", "quinta", "sexta"]:
    dist = float(input(f"Insira a distância percorrida na {dia}"))
    temp = float(input(f"Insira o tempo da viagem da {dia}"))
    velocidades_medias.append(velocidade_media(dist, temp))

print(f"As velocidades médias da semana foram {velocidades_medias}")