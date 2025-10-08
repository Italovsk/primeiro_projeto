def calcular_ir_resgate():
#1. RECEBIMENTO E VALIDAÇÃO DO TIPO DE INVESTIMENTO

    tipo_investimento = 0

    print("Escolha o tipo de investimento:")
    print("1. CDB")
    print("2. LCI")
    print("3. LCA")

    # Loop para garantir que o tipo de investimento seja 1, 2 ou 3
    while tipo_investimento not in [1, 2, 3]:
        entrada = input("Digite o tipo de investimento (1, 2 ou 3): ")

        # Validação simples de número inteiro
        if entrada.isdigit():
            tipo_investimento = int(entrada)
            if tipo_investimento not in [1, 2, 3]:
                print("Escolha inválida! Digite 1, 2 ou 3.")
        else:
            print("Entrada inválida. Digite apenas o número da opção.")

#2. RECEBIMENTO E VALIDAÇÃO DE VALOR E DIAS

    # Recebe e valida o valor do resgate
    valor_resgate = 0.0
    while valor_resgate <= 0.0:
        entrada = input("Digite o valor a ser resgatado: ")
        if entrada.replace('.', '', 1).isdigit():
            valor_resgate = float(entrada)
            if valor_resgate <= 0.0:
                print("O valor do resgate deve ser maior que zero.")
        else:
            print("Entrada inválida. Digite um valor numérico válido.")

    # Recebe e valida o número de dias
    dias_investidos = 0
    while dias_investidos <= 0:
        entrada = input("Digite o número de dias que o valor permaneceu investido: ")
        if entrada.isdigit():
            dias_investidos = int(entrada)
            if dias_investidos <= 0:
                print("O número de dias deve ser maior que zero.")
        else:
            print("Entrada inválida. Digite um número inteiro.")

#3. CÁLCULO DO IMPOSTO DE RENDA (IR)

    aliquota_ir = 0.0

    # LCI (2) e LCA (3) são ISENTOS de imposto de renda.
    if tipo_investimento == 2 or tipo_investimento == 3:
        aliquota_ir = 0.0

    # CDB (1) é TRIBUTÁVEL e depende do número de dias.
    elif tipo_investimento == 1:

        # Estrutura IF/ELIF para determinar a alíquota baseada nos dias
        if dias_investidos <= 180:
            aliquota_ir = 0.225  # 22,5%
        elif dias_investidos <= 360:  # De 181 a 360 dias
            aliquota_ir = 0.20  # 20%
        elif dias_investidos <= 720:  # De 361 a 720 dias
            aliquota_ir = 0.175  # 17,5%
        else:  # Acima de 720 dias
            aliquota_ir = 0.15  # 15%

# Cálculo final
    valor_imposto = valor_resgate * aliquota_ir

#4. SAÍDA FINAL

#A saída formatada conforme o modelo
    print(f"O valor do imposto de renda a ser pago é: R$ {valor_imposto:.2f}")


#Executa a função principal
if __name__ == "__main__":
    calcular_ir_resgate()