"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
minha soluçãoÇ
lista = ['Maria', 'Helena', 'Luiz', False, True, 1.25, -5]
tamanho = len(lista)
j = 0
while j < tamanho:
    for i in lista:
        print(f'valor: {i}, índice: {j}')
        j += 1
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))