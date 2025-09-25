#Pedir ao usuário os minutos atuais
minutos = int(input("Por favor insira a quantidade de minutos atuais: "))
#Calcular o fatorial
resultado_fatorial = 1
for i in range(1, minutos +1):
    resultado_fatorial = resultado_fatorial * i

#Exibir senha necessária para desbloqueio
senha = "LIBERDADE" + str(resultado_fatorial)
print("A senha para desbloquear o servidor é:", senha)
