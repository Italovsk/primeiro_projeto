def calcular_parcelamento_divida():

#1. RECEBIMENTO E VALIDAÇÃO DO VALOR DA DÍVIDA

    valor_divida = 0.0

    # Loop para garantir que o usuário digite um valor numérico positivo
    while valor_divida <= 0.0:
        entrada = input("Digite o valor da dívida: ")

        # Validação simples de se a entrada é um número (aceita ponto decimal)
        if entrada.replace('.', '', 1).isdigit():
            valor_divida = float(entrada)
            if valor_divida <= 0.0:
                print("O valor da dívida deve ser maior que zero.")
        else:
            print("Entrada inválida. Digite um valor numérico válido.")

    #2. DADOS DO PARCELAMENTO (Tabela)

    # Lista de opções de parcelas
    parcelas_opcoes = [1, 3, 6, 9, 12]

    # Lista de % de juros sobre o valor INICIAL da dívida (na ordem correspondente)
    # 0, 10, 15, 20, 25
    juros_percentual = [0.0, 0.10, 0.15, 0.20, 0.25]  # Convertidos para decimal

#3. CÁLCULO E TABELA DE SAÍDA

    # Usamos o loop 'for' para percorrer as 5 opções da tabela
    #range(len(parcelas_opcoes)) garante que percorreremos de 0 a 4
    for i in range(len(parcelas_opcoes)):
        # Obtém os dados da iteração atual
        qtd_parcelas = parcelas_opcoes[i]
        juros_taxa = juros_percentual[i]

        # CÁLCULOS

        # Valor dos Juros (calculado sobre o valor INICIAL da dívida)
        valor_juros = valor_divida * juros_taxa

        # Valor Total (Dívida + Juros)
        valor_total = valor_divida + valor_juros

        # Valor da Parcela
        valor_parcela = valor_total / qtd_parcelas

        # SAÍDA (Formatada conforme o modelo)
        # Usamos :.2f para formatar os valores monetários com 2 casas decimais
        print(
            f"Total:R$ {valor_total:.2f} "
            f"Juros:R$ {valor_juros:.2f} "
            f"Número de parcelas:{qtd_parcelas} "
            f"Valor da Parcela:R$ {valor_parcela:.2f}"
        )


# Executa a função principal
if __name__ == "__main__":
    calcular_parcelamento_divida()