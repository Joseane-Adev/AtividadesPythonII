#exercicios

perguntas = [
    {
        'Pergunta': 'Quanto é 10 + 2',
        'opçoes': ['1', '12', '4', '6'],
        'resposta': '12',
    },      
    {
        'Pergunta': 'Quanto é 10 * 2',
        'opçoes': ['1', '20', '4', '6'],
        'resposta': '20',

    }
]

for pergunta in perguntas:
    print('Pergunta: ',pergunta['Pergunta'])
    print()

    opçoes = pergunta['opçoes']
    for i, opcao in enumerate(opçoes):
        print(f'{i} :', opcao)

    escolha = input('Digite sua escolha')

    acertou = False
    escolha_inteiro = None
    quantidade_opçoes = len(opçoes)

    if escolha.isdigit():
        escolha_inteiro = int(escolha)

    if escolha_inteiro is not None:
        if escolha_inteiro >= 0 and escolha_inteiro < quantidade_opçoes:
            if opçoes[escolha_inteiro] == pergunta['resposta']:
                acertou = True
    
    if acertou:
        print('Acertou')
    else:
        print('Errou')