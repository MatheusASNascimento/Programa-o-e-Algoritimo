################################################################
# Descrição: Um programa que pede dois números e mostra o maior.
# Parâmetros de entrada: Dois números digitados pelo usuário.
# Valores de saída: O maior número informado.
# Autor:Matheus Augusto da Silva Nascimento
################################################################
n1= float(input("Digite o primeiro número:"))
n2= float(input("Digite o segundo número:"))
if n1 > n2:
    print("O maior número é:", n1)
elif n2 > n1:
    print("O maior número é:", n2)
else:
    print("Os dois números são iguais!")