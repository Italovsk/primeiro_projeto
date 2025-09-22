rm = input("Por favor, insira o seu RM: ")
idade = int(input("Por favor, insira a sua idade: "))

if idade >= 18:
    print(f"Seu cadastro foi finalizado, aluno de RM {rm}")
    print("Os detalhes serão enviados para o seu e-mail!")

else:
    autorização = input("Você tem autorização dos seus pais? S- SIM, N- NÃO: ")
    if autorização == "S":
        print(f"Sua participação foi autorizada, aluno de RM{rm}")
        print("Mais informações serão enviadas para o e-mail dos responsáveis")
    else:
        print("Seu cadastro não pôde ser concluído")
print("O programa será finalizado")
