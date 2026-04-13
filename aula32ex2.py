"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

H = int(input('Digite a hora: '))
if H >= 0 and H <= 11:
    print('Bom dia')
elif H >= 12 and H <=17:
    print('Boa tarde')
elif H >= 18 and H <= 23:
    print('Boa noite')
else:
    print('Hora digitada inválida')        