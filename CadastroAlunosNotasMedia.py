N = int(input("Quantos alunos serão cadastrados: "))
nome = [""] * N
cpf = [""] * N
email = [""] * N
matricula = [""] * N
nota1 = [""] * N
nota2 = [""] * N
nota3 = [""] * N
media = [""] * N
nota4 = [""] * N
mediaNova = [""] * N


for i in range(N):
    nome[i] = input("Digite o nome do aluno: ")
    cpf[i] = input("Digite o cpf do aluno: ")
    email[i] = input("Digite o Email do aluno: ")
    matricula[i] = input("Digite a Matrícula do aluno: ")
    nota1[i] = float(input("Digite a primeira nota do aluno: "))
    nota2[i] = float(input("Digite a segunda nota do aluno: "))
    nota3[i] = float(input("Digite a terceira nota do aluno: "))
    media[i] = (nota1[i] + nota2[i] + nota3[i]) / 3

for i in range(N):
    if media[i] < 6:
        nota4[i] = float(input(f"Qual a nota adicional do aluno {nome[i]}:"))
        mediaNova[i] = (nota1[i] + nota2[i] + nota3[i] + nota4[i]) / 4
    else:
        mediaNova[i] = 0

for i in range(N):
    if media[i] >= 6:
        print(nome[i], cpf[i], email[i], matricula[i], media[i])
        print("Aprovado!")
        
    elif mediaNova[i] >= 6:
        print(nome[i], cpf[i], email[i], matricula[i], mediaNova[i])
        print("Aprovado!")
        
    else:
        print(nome[i], cpf[i], email[i], matricula[i], mediaNova[i])
        print("Reprovado")
        