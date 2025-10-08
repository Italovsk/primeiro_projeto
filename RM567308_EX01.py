def realizar_votacao_elementar():

#VARIÁVEIS DE CONTAGEM
    cont_segunda = 0
    cont_terca = 0
    cont_quarta = 0
    cont_quinta = 0
    cont_sexta = 0

#RECEBIMENTO E VALIDAÇÃO DO NÚMERO DE COLABORADORES
    num_colaboradores = 0
#Loop continua enquanto o número de colaboradores não for válido (> 0)
    while num_colaboradores <= 0:
        entrada = input("Informe o número de colaboradores: ")
        if entrada.isdigit():
            num_colaboradores = int(entrada)
            if num_colaboradores <= 0:
                print("O número deve ser maior que zero.")
        else:
            print("Entrada inválida. Digite apenas números inteiros.")

#2. COLETA DOS VOTOS

    colaborador_atual = 1

    while colaborador_atual <= num_colaboradores:

#Inicializa a variável de voto com um valor que a condição inicial NÃO aceita
        voto_atual = "invalido"

#Loop para validar a entrada do voto
        while voto_atual != "segunda-feira" and \
                voto_atual != "terça-feira" and \
                voto_atual != "quarta-feira" and \
                voto_atual != "quinta-feira" and \
                voto_atual != "sexta-feira":

#Pede o voto
            prompt = "Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): "
            voto_atual = input(prompt).lower().strip()

#Mensagem de erro se a condição for verdadeira novamente
            if voto_atual != "segunda-feira" and \
                    voto_atual != "terça-feira" and \
                    voto_atual != "quarta-feira" and \
                    voto_atual != "quinta-feira" and \
                    voto_atual != "sexta-feira":
                print("Dia inválido! Tente novamente.")

#3.Contagem
        if voto_atual == "segunda-feira":
            cont_segunda = cont_segunda + 1
        elif voto_atual == "terça-feira":
            cont_terca = cont_terca + 1
        elif voto_atual == "quarta-feira":
            cont_quarta = cont_quarta + 1
        elif voto_atual == "quinta-feira":
            cont_quinta = cont_quinta + 1
        elif voto_atual == "sexta-feira":
            cont_sexta = cont_sexta + 1

#Incrementa o contador do colaborador para a próxima repetição
        colaborador_atual = colaborador_atual + 1

#4. DETERMINAÇÃO DO VENCEDOR E EMPATE

#4.1. Encontra o máximo de votos
    max_votos = cont_segunda

    if cont_terca > max_votos:
        max_votos = cont_terca
    if cont_quarta > max_votos:
        max_votos = cont_quarta
    if cont_quinta > max_votos:
        max_votos = cont_quinta
    if cont_sexta > max_votos:
        max_votos = cont_sexta

#4.2. Verifica quem atingiu o máximo (Tratando Empate)

    dias_vencedores = ""
    num_vencedores = 0

    if cont_segunda == max_votos and max_votos > 0:
        dias_vencedores = "segunda-feira"
        num_vencedores = num_vencedores + 1

    if cont_terca == max_votos and max_votos > 0:
        if num_vencedores > 0:
            dias_vencedores = dias_vencedores + ", terça-feira"  # Adiciona com vírgula para empate
        else:
            dias_vencedores = "terça-feira"
        num_vencedores = num_vencedores + 1

    if cont_quarta == max_votos and max_votos > 0:
        if num_vencedores > 0:
            dias_vencedores = dias_vencedores + ", quarta-feira"
        else:
            dias_vencedores = "quarta-feira"
        num_vencedores = num_vencedores + 1

    if cont_quinta == max_votos and max_votos > 0:
        if num_vencedores > 0:
            dias_vencedores = dias_vencedores + ", quinta-feira"
        else:
            dias_vencedores = "quinta-feira"
        num_vencedores = num_vencedores + 1

    if cont_sexta == max_votos and max_votos > 0:
        if num_vencedores > 0:
            dias_vencedores = dias_vencedores + ", sexta-feira"
        else:
            dias_vencedores = "sexta-feira"
        num_vencedores = num_vencedores + 1

#5. EXIBE O RESULTADO FINAL
    if num_vencedores == 1:
        # A única linha de saída exigida no modelo
        print(f"O dia escolhido pelos colaboradores é: {dias_vencedores}")
    elif num_vencedores > 1:
        # Tratamento de Empate (conforme solicitado no enunciado original)
        print(f"ATENÇÃO: Houve empate ({max_votos} votos) entre os dias: {dias_vencedores}")
        print("O dia escolhido pelos colaboradores é: Indefinido (Empate)")
    else:
        print("Nenhum voto foi registrado.")


# Executa o programa
if __name__ == "__main__":
    realizar_votacao_elementar()