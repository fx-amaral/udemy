# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
pessoa.setdefault('nome do meio', "Sant'Anna")
<<<<<<< HEAD
# print(pessoa['idade'])
# print(pessoa)
# print(pessoa['nome do meio'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
print(list(pessoa.items()))
=======
print(pessoa['idade'])
print(pessoa)
print(pessoa['nome do meio'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
>>>>>>> 83932bf9f8461cce31e57ff0e521d1245ad00e9c

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)