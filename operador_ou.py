#Durante o aniversário de sua fundação, uma loja está presenteando clientes da seguinte forma:
#Todas as compras de valor superior à R$1000, receberão um desconto de 10%
#Clientes selecionados receberam o cupom FESTA, que gera 10% de desconto na hora da compra, não importando o valor.
#Os descontos não são cumulativos.
#Escreva um script em python que receba um cupom e o valor de uma compra do usuário e informe o valor da compra

valor_compra = float(input("Por favor informe o valor da compra realizada: "))
cupom = input("Digite um cupom válido: ")

if valor_compra >= 1000 or cupom == "FESTA":
    valor_compra = valor_compra * 0.9
else:
    print("Compra sem desconto!")

print(f"A sua compra teve o valor de R${valor_compra}")
