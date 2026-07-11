# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
from dados import produtos # package dados, modulo produtos_modulo, variável produtos
import copy

novos_produtos = [
                    {**p, 'preco': round(p['preco']*1.1, 2)}#aumento de 10% de cada item na chave preco
                    for p in copy.deepcopy(produtos)#cópia profunda do dicionário
                 ] 


print(*produtos, sep=('\n')) #imprime lista de todos os itens do dict separados por linha
print()
print(*novos_produtos, sep=('\n'))
print()
for p in novos_produtos:
     print(f"Nome: {p['nome']} | Preço: {p['preco']:.2f}")
print()
print()
 


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
                                        copy.deepcopy(produtos),
                                        key=lambda  p: p['nome'],
                                        reverse=True
                                    )

print(*produtos_ordenados_por_nome, sep=('\n'))
print()
for p in produtos_ordenados_por_nome:
     print(f"Nome: {p['nome']} | Preço: {p['preco']:.2f}")
print()
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
                                        copy.deepcopy(produtos),
                                        key=lambda p: p['preco']
                                    )

print()
print(*produtos_ordenados_por_preco, sep=('\n'))
print()

for p in produtos_ordenados_por_preco:
     print(f"Nome: {p['nome']} | Preço: {p['preco']:.2f}")