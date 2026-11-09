################################################################
# Descrição: Identifica o turno em que o aluno estuda.
# Parâmetros de entrada: Uma letra M = Matutino, T = Tarde , N = Noturno.
# Valores de saída: Bom Dia, Boa Tarde, Boa Noite ou
# Valor Inválido.
# Autor: Matheus Augusto da Silva Nascimento
################################################################
turno = input("Digite M para Matutino, T para tarde ou N para Noturno: ")
turno = turno.upper()
if turno == "M":
    print("Bom Dia")
elif turno == "V":
    print("Boa Tarde")
elif turno == "N":
    print("Boa Noite")
else:
    print("Valor Inválido")