rm = input("Por favor, insira o seu RM: ")
idade = int(input("Por favor, insira a sua idade: "))

if idade >= 18:
    print(f"Seu cadastro foi finalizado, aluno de RM {rm}")
    print("Os detalhes serão enviados para o seu email!")

else:
    print("Seu cadastro não pôde ser concluído")
print("O programa será finalizado")
