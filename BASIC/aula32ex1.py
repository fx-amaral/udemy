I = (input('Digite um nº inteiro: '))

if I.isdigit():
    I = int(I)
    I = I % 2
    if I == 0:
        print('É par')
    else:
        print('É impar')
else: 
    print(f'{I} não é um inteiro')   
     