def soma(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + soma(lista[1:])



N = int(input())
lista = input().split()

for i in range(N):
    lista[i] = int(lista[i])
    
#lista = [4, 2, 3, 1, 20]
print(soma(lista))