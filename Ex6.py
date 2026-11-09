################################################################
# Descrição: Apresentar os quadrados dos números inteiros
# existentes na faixa de valores de 15 a 200.
#
# Parâmetros de entrada: Não possui entrada de dados.
#
# Valores de saída: O quadrado de cada número inteiro
# de 15 até 200.
#
# Autor: Matheus Augusto da Silva Nascimento
################################################################
for num in range(15, 201):
    q = num ** 2
    print(num, "ao quadrado é:", q)
