# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicador(num):
    def multiplica(valor):
        return num * valor
    return multiplica
        
valor_dobro = multiplicador(2)   
valor_triplo = multiplicador(3)
valor_quadruplo = multiplicador(4)

print(valor_dobro(10))
print(valor_triplo(22))
print(valor_quadruplo(5))  