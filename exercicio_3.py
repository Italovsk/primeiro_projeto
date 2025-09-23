voto1 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO")
voto2 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO")
voto3 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO")
voto4 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO")
votO5 = input("Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO")

playstation = 0
xbox = 0
nintendo = 0

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 2 digitou um console inexistente e seuvoto será desconsiderado")

if playstation > xbox and playstation > nintendo:
    print("O console escolhido foi playstation")
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi o Nintendo")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi nintendo")
else:
    print("Houve empate, favor entrar em contato com a direção")
