valor_bruto = float(input("Por favor, informe o valor bruto da viagem: "))
categoria = input("Por favor, informe a categoria: ECONÔMICA, EXECUTIVA ou PRIMEIRA CLASSE: ")
quantidade_viajantes = int(input("Por favor, informe a quantidade de viajantes: "))

valor_desconto = 0
if categoria.upper() == "ECONÔMICA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.03
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.04
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.05
elif categoria.upper() == "EXECUTIVA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.05
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.07
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.08
elif categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.1
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.15
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.2
else:
    print("Categoria inexistente, nenhum desconto aplicado")

valor_liquido = valor_bruto - valor_desconto
media_viajante = valor_liquido / quantidade_viajantes

print("O valor da viagem é de R${}. Após os descontos de R${}, a viagem custará R${}. Cada passageiro tem um custo médio de R${}".format(valor_bruto, valor_desconto, valor_liquido, media_viajante))