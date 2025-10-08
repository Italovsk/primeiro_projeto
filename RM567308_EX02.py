def calcular_parcelamento():
#1. RECEBIMENTO E VALIDAÇÃO DO PREÇO DO CARRO
    preco_carro = 0
#Loop para garantir que o usuário digite um valor numérico positivo
    while preco_carro <= 0:
        entrada = input("Digite o preço do carro: ")

#Validação simples de se é um número inteiro ou float
        if entrada.replace('.', '', 1).isdigit():
            preco_carro = float(entrada)
            if preco_carro <= 0:
                print("O preço deve ser maior que zero.")
        else:
            print("Entrada inválida. Digite um valor numérico válido.")

#2. CÁLCULO À VISTA (com 20% de Desconto)

    desconto = 0.20  # 20%
    preco_vista = preco_carro * (1 - desconto)

#Exibe o preço à vista
    print(f"O preço final á vista com desconto 20% é: {preco_vista:.2f}")

#3. CÁLCULO E TABELA DE PARCELAMENTO

#Lista de parcelas (para ser percorrida pelo laço for)
    parcelas_opcoes = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]

#Lista de acréscimos (em % e na ordem correspondente a parcelas_opcoes)
    acrescimos_percentual = [0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21, 0.24, 0.27, 0.30]

    # Usamos o loop 'for' para percorrer as opções de parcelamento
    for i in range(len(parcelas_opcoes)):
        # Obtém os dados da iteração atual
        qtd_parcelas = parcelas_opcoes[i]
        acrescimo = acrescimos_percentual[i]  # Ex: 0.03 (para 6x), 0.06 (para 12x), etc.

        # Cálculo do Preço Final
        preco_final_parcelado = preco_carro * (1 + acrescimo)

        # Cálculo do Valor da Parcela
        valor_parcela = preco_final_parcelado / qtd_parcelas

        print(
            f"O preço final parcelado em {qtd_parcelas} X é de R$ {preco_final_parcelado:.2f} com parcelas de R$ {valor_parcela:.2f}")


# Executa a função principal
if __name__ == "__main__":
    calcular_parcelamento()