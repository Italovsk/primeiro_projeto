#Pedir ao usuário quantas transações financeiras ele realizou ao longo de um dia e na sequência informar o valor de cada uma
total_gasto = 0
media_transacao = 0
quantidade_transacoes = int(input("Quantas transações você realizou hoje?"))

for i in range(quantidade_transacoes):
        valor_transacao = float(input(f"Qual o valor da transação {i+1}"))
#Adicionar o valor da transação ao total_gasto
        total_gasto += valor_transacao
media_transacao = total_gasto / quantidade_transacoes
#Exibir ao final o valor total gasto pelo usuário, e uma média do valor de cada transação
print("O total gasto hoje foi de: ", total_gasto)
print("O valor médio por transação foi de:", media_transacao)
