'''Exemplo de uso de tabelas hash'''



def verifica_eleitor(nome):
    if voted.get(nome):
        print('Mande embora!')
    else:
        voted[nome] = True
        print('Deixe votar!')

voted = {}

while True:
    eleitor = input('Digite o nome do eleitor para verificação: ')
    verifica_eleitor(eleitor)
    #print(voted)
    if eleitor == 'sair':
        break
print(voted) 