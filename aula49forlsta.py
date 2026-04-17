"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz', False, True, 1.25, -5]
tamanho = len(lista)
j = 0
while j < tamanho:
    for i in lista:
        print(f'valor: {i}, índice: {j}')
        j += 1
    #j += j.append()
    #print(j)
        
    #print(nome, type(nome))
