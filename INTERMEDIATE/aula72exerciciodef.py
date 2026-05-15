# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult (*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par_impar(x):
    resto = x%2 == 0
    if resto :
       return f'{x} é par'
    return f'{x} é impar'    

seq = 5,10,3,4,8
prod = mult(*seq)
print(prod)

#num = int(input())
print(par_impar(10))

#versão par_impar do professor

def par_impar (numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

print(par_impar(16))