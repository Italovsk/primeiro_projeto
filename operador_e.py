#Para acessar um sistema, o usuário deve digitar o username darth_vader e a senha 1123
#Crie um script que receba e valide estas informações de acesso

username = input("Digite o seu nome de usuário: ")
senha = input("Digite a senha deste usuário: ")

if username.lower() == "darth_vader" and senha == "1123":
    print("Login bem-sucedido!")
else:
    print("Login não autorizado!")
