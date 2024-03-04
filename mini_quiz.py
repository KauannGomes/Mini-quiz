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
acertos = 0 
c = 0
for perguntas in perguntas:
    print(perguntas['Pergunta'])
    c +=1

    for i, op in enumerate(perguntas['Opções']):
        print((f'{i}) {op}'))
    while True:
        try:
            resposta = perguntas['Opções'][int(input('Escolha uma opção: '))]
            break
        except :
            print('Digite um index valido')
            print(perguntas['Pergunta'])
            for i, op in enumerate(perguntas['Opções']):
                print((f'{i}) {op}'))
    if resposta == perguntas['Resposta']:
        print('Voce acertou ✔️')
        print()
        acertos += 1
    else:
        print('Voce errou ❌')  
        print()
print('-='*30)    
print(f'Voce acertou {acertos} de {c} perguntas')
print('-='*30)    