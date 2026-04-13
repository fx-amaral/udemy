def maiorv (lista):
    if len(lista) == 0:
        return print('lista vazia')
    elif len(lista) == 1:
        return lista[0]
    else:
        temp = maiorv(lista[1:])
        if lista[0] > temp:
            return lista[0]
        else:
            return temp

#N = int(input())
#lista = input().split()

lista = [4, 5, 6, 2100, 10, 1]  
print(maiorv(lista))      
        
