numero_combo = int(input("Digite o número do combo desejado: "))

match numero_combo:
    case 1:
        nome_prato = "Hamburguer"
        valor_prato = 12.50
    case 2:
        nome_prato = "Cheeseburguer"
        valor_prato = 15.00
    case 3:
        nome_prato = "X-bacon"
        valor_prato = 21.00
    case _:
        nome_prato = None
        valor_prato = None
if nome_prato:
    print(f"O combo desejado é {nome_prato} e custa {valor_prato}")