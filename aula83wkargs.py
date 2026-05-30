# Empacotamento e desempacotamento de dicionários
a, b = 1, 2 #empacotou a tupla 1 pr cd variável
a, b = b, a #desempacotou trocando os valores
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)
val = [1,3,9,3,8,5]
val2 = sum(val)
print(val2)
print()
print()
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
    'chave_teste' : 'testado',
}
mostro_argumentos_nomeados(val, 1 , val2, 5,  **configuracoes)
print()
print()
print(configuracoes)
print()
tudao = {**pessoas_completa, **configuracoes}
for chave, valor in tudao.items():
    print(chave, valor)
