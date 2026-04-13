frase = 'Uma coisa morta pode seguir a correnteza, mas somente uma coisa viva pode contrariá-la - G K Chesterton'

qtd = 0
qtd_maior = 0
letra = ''
letra_maior_ocorrencia = ''
i = 0

while i < len(frase):
    letra = frase[i]
    if letra == ' ':
        i += 1
        continue
        
    qtd = frase.count(letra)
    if qtd > qtd_maior:
        qtd_maior = qtd
        letra_maior_ocorrencia = letra
    
    i += 1
    
print(letra_maior_ocorrencia , qtd_maior )
#print(letra, qtd)



#print(qtd)