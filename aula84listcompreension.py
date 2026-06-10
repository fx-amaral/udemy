# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
print(tuple(range(29)))
print()
lista = []                     
for numero in range(10): #criando lista com for
    lista.append(numero)
print(lista)

lista = [
    numero * 2
    for numero in lista   #range(10) #list comprehension
]
print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
] 
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print()
print('produtos', *produtos, sep='\n')
print()
print('produtos novos', *novos_produtos, sep='\n')