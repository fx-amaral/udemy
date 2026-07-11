# dir, hasattr e getattr em Python

import aula71args
string = 'casa'
metodo = 'upper'

print('Módulo - ',__name__)

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(metodo, metodo)())
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)