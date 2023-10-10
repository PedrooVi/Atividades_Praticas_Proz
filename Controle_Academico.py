turma = []
menu = True
disciplinas = ["1 Algoritmos, 2 Segurança, 3 Desenvolvimento Web"]


# Função para cadastrar um aluno
def cadastro_aluno():
    if len(turma) >= 15:
        print(
            "Limite máximo de 15 alunos atingido. Não é possível cadastrar mais alunos."
        )
        return

    aluno = {}
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["matricula"] = int(input("Digite a matrícula do aluno: "))
    aluno["notas"] = {
        disciplina: [0.0] * 5 for disciplina in disciplinas.values()
    }  # Inicializa as notas com zeros
    turma.append(aluno)
    print("Aluno cadastrado com sucesso!")


# Função para encontrar um aluno na lista com base na matrícula
def encontrar_aluno(matricula):
    for aluno in turma:
        if aluno["matricula"] == matricula:
            return aluno
    return None


# Função para adicionar notas a um aluno
def adicionar_notas():
    matricula = int(input("Digite a matrícula do aluno: "))
    aluno = encontrar_aluno(matricula)

    if aluno is not None:
        cod_disc = int(
            input(
                "Digite o código da disciplina ([1]Algoritmos; [2]Segurança; [3]Desenvolvimento Web): "
            )
        )

        if cod_disc in disciplinas:
            for nota in range(5):
                mensagem = ("INFORME A NOTA", nota + 1)
                nota_temporaria = float(input(mensagem))
                while not (0 <= nota_temporaria <= 10):
                    nota_temporaria = float(
                        input("Nota inválida. Informe uma nota entre 0 e 10: ")
                    )
                aluno["notas"][disciplinas[cod_disc]][nota] = nota_temporaria
            print("Notas adicionadas com sucesso!")
        else:
            print("Código de disciplina inválido.")
    else:
        print("Aluno com a matrícula informada não encontrado.")


# Função para mostrar as informações de um aluno
def consultar_informacoes():
    matricula = int(input("Digite a matrícula do aluno: "))
    aluno = encontrar_aluno(matricula)

    if aluno is not None:
        print("Informações do aluno:")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Matrícula: {aluno['matricula']}")
        for cod_disc, nome_disc in disciplinas.items():
            print(f"Notas de {nome_disc}: {aluno['notas'][nome_disc]}")
    else:
        print("Aluno com a matrícula informada não encontrado.")


# Menu principal
while menu == True:
    print("\nBEM VINDO AO PORTAL DA ESCOLA!")
    print("O que você deseja?")
    print("[1]Cadastrar alunos;")
    print("[2]Incluir notas;")
    print("[3]Consultar informações;")
    print("[4]Sair.")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastro_aluno()
    elif opcao == "2":
        adicionar_notas()
    elif opcao == "3":
        consultar_informacoes()
    elif opcao == "4":
        menu = False
    else:
        print("Opção inválida. Tente novamente.")

# Estudos feitos por aulas presenciais e aulas no Youtube.
