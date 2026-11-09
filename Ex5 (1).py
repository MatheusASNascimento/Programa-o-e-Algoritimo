################################################################
# Descrição: Calcula a média de duas notas e informa a situação
# do aluno.
# Parâmetros de entrada: Duas notas de alunos.
# Valores de saída: Média e situação final do aluno.
# Autor: Matheus Augusto da Silva Nascimento
################################################################
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

print("Sua média é:", media)

if media == 10:
    print("Aprovado com Distinção!")
elif media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")