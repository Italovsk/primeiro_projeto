#valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5, 3.5]
#exibição da lista
print("A lista foi criada assim: {}".format(valores))

#contagem de elementos 1

contagem = valores.count(1)
print(f"A contagem de números 1 foi de {contagem}")
#invertendo a lista
valores.reverse()
print(f"A lista invertida ficou assim: {valores}")
#ordenando a lista
valores.sort(reverse = True)

print(f"A lista em ordem decrescente ficou assim: {valores}")
#tamanho da lista
quantidade = len(valores)
print(f"A quantidade de elementos na lista é {quantidade}")
#Soma dos elementos
soma = sum(valores)
print(f"A soma dos valores é {soma}")