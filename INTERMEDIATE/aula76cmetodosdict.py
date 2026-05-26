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
    'nome do meio': "Sant'Anna",
    'idade': 900,
}

#print(list(pessoa.keys()))
pessoa.setdefault('altura', 1.80)
# print(pessoa['altura'])
# print(len(pessoa))
#print(list(pessoa.keys()))
# print(list(pessoa.values()))
lista = (list(pessoa.items()))
print(list(pessoa.items()))
print(lista[0][1])

# for valor in pessoa.values():
#     print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)