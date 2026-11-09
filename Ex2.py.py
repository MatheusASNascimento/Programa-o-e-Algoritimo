################################################################
# Descrição:O programa verifica se um número é positivo ou negativo.
# Parâmetros de entrada: Um número digitado pelo usuário.
# Valores de saída: Informa se o número é positivo, negativo
# ou igual a zero.
# Autor: Matheus Augusto da Silva Nascimento
################################################################
n= float(input("Digite um número: "))
if n > 0:
    print("O número é positivo!")
elif n < 0:
    print("O número é negativo!")
else:
    print("O número é igual a zero!")