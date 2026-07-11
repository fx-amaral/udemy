print('Este módulo se chama', __name__)

variavel_modulo = 'Fábio'

print(variavel_modulo)

def soma(x, y):
    return x + y

from sys import path
print(*path, sep=('\n'))