def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = []
        maiores = []
        i = 0       
        for i in array[1:]:
            '''menores = [i for i in array[1:] if i <= pivo]
            maiores = [i for i in array[1:] if i > pivo]'''
            if i <= pivo:                
                menores.append(i)
            else:
                maiores.append(i)
        '''array = [quicksort(menores) + [pivo] + quicksort(maiores)]
    return array'''
        return quicksort(menores) + [pivo] + quicksort(maiores)
            
#program
N = int(input('Quantidade de elementos: '))
lista = input().split()
i = 0
for i in range(N):
    lista[i] = int(lista[i])
print(f'lista digitada : {lista}')
#quicksort(lista) 
print(f'lista ordenada: {quicksort(lista)}')