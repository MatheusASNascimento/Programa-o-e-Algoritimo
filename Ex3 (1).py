################################################################
# Descrição: Identifica o sexo de acordo com a letra digitada.
# Parâmetros de entrada: Uma letra f ou m.
# Valores de saída: Feminino, Masculino ou Sexo Inválido.
# Autor: Matheus Augusto da Silva Nascimento
################################################################
sex = input("Digite F para Feminino ou M para Masculino: ")
sex = sex.upper()
if sex == "F":
    print("O Sexo é feminino")
elif sex == "M":
    print("O Sexo é Masculino")
else:
    print("Sexo Inválido!")