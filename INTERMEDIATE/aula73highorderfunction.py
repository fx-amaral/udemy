"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome, nome1, nome2):
    #return saudacao
    return f'{msg}, {nome}, {nome1}, {nome2} !'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz', 'teste', 'maisum')
)
print(
    executa(saudacao, 'Boa noite', 'Maria', 'testa?', 'maisum')
)

# c = executa(saudacao, 'arg1', 'arg2', 'arg3', 'arg4')
# print(c)

# c = saudacao()
# print(c())