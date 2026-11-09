################################################################
# Descrição: Mostrar os resultados da tabuada 
# qualquer, apresentando cada resultado
# Parâmetros de entrada: Um número informado pelo usuário.
# Valores de saída: A tabuada do número informado.
# Autor: Matheus Augusto da Silva Nascimento
################################################################
num = int(input("Digite um número: "))
for i in range(1, 11):
    r = num * i
    print(num, "x", i, "=", r)