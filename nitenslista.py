def n_itens (lista):
    if lista == []:
        return 0
    else:
        return 1 + n_itens(lista[1:])
    

lista = [1, 7, 6 , 4, 0, 9, 0, 25, 10]
print(n_itens(lista))