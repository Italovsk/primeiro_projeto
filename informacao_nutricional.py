#Pedir ao usuário quantos alimentos consumiu no dia
quantidade_alimentos = int(input("Quantos alimentos você consumiu no dia de hoje?"))
#Inicializar uma variável para guardar o total de calorias, começando em zero
total_calorias = 0
#Usar um loop para perguntar as calorias de cada alimento
for i in range(quantidade_alimentos):
    calorias_alimento = int(input(f"Quantas calorias o alimento {i+1} tem? "))
    total_calorias = total_calorias + calorias_alimento
#Exibir o total de calorias no final
print("O seu consumo total de calorias diárias é:", total_calorias)


