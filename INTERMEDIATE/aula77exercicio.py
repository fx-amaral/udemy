# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

#Solução professor
qtd_acertos = 0

for pergunta in perguntas:
        print(f'Pergunta : {pergunta['Pergunta']}')
        print()
        opcoes = pergunta['Opções']
        for i, opcao in enumerate(opcoes):
            print(f'{i})', opcao)
                      
        print()
        resp = input('Escolha uma opção : ')
        resp_int = None
        qtd_opcoes = len(opcoes)
        if resp.isdigit():
            resp_int = int(resp)
               
        if resp_int is not None:
             if resp_int >= 0 and resp_int < qtd_opcoes:
                  if opcoes[resp_int] == (pergunta['Resposta']):
                       qtd_acertos += 1
                       print('acertou')
                       
                  else:
                       print('errou')  


        print()
        print('Você acertou', qtd_acertos)
        print('de', len(perguntas),'Perguntas')

        print()