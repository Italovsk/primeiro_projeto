#pedir duas varíaveis ao usuário
print("Esse programa inverte os conteúdos de duas variáveis")
A = input("Digite o conteúdo da variável A: ")
B = input("Digite o conteúdo da variável B: ")
#trocar os valores
troca = A
A = B
B = troca
print(f"Agora que trocamos, a variável A contém {A} e a variável B contém {B}")
