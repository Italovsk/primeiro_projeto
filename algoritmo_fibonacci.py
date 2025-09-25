#Pedir ao usuário um valor numérico inteiro
valor = int(input("Por favor insira seu número"))
#Variáveis
termo1 = 0
termo2 = 1
#Casos especiais se o usuário usar 0 ou 1, que estão no começo da sequência
if valor == 0 or valor == 1:
    print("Ação bem-sucedida!")
else:
#Criar um loop while para continuar enquanto a condição for verdadeira.
    while termo2 < valor:
        proximo_termo = termo1 + termo2
        termo1 = termo2
        termo2 = proximo_termo
#Caso o número esteja na sequência, o algoritmo deve exibir a mensagem "Ação bem-sucedida!", e caso não esteja, deve exibir uma mensagem "A ação falhou..."
if termo2 == valor:
        print("Ação bem-sucedida!")
else:
    print("A ação falhou...")