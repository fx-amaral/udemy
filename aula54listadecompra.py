# Execício - Criar lista de compras
import os

lista_compras = []

while True:
    opcao = input('Eacolha uma opçao: [i]nserir [a]pagar [l]istar   ')
    
    
    if opcao == 'i':
        os.system('cls')                        
        valor = input('valor:')
        lista_compras.append(valor)
        #print('i')
    elif opcao == 'a':
        try:
            indice = int(input('Escolha um índice para apagar: '))
            del lista_compras[indice]
        except ValueError:
            print('Para apagar um ítem. Digite um número inteiro positivo')
        except IndexError:
            print('Indice fora da lista')
    elif opcao == 'l':
        os.system('cls')
        #print ('l')
        if len(lista_compras) == 0:
            print('Lista vazia')
        
        for i,valor in enumerate(lista_compras):
            print(i, valor)
    else:
        print('Por favor escolha i  a ou l')