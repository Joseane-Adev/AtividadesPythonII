#sitema de notas

notas = []

while True:

    aluno = input('Digite seu nome: ')
    nota1= int(input('Digite sua nota de trabalho: '))
    nota2= int(input('Digite sua nota de prova: '))


    if nota1 == 0 and nota2 == 0:
        print(f'{aluno},você não tem nota suficiente!')
        break
    else:
        notas.append(nota1)
        notas.append(nota2)
    
    media = (nota1+ nota2) / 2 #contador de notas

    print(notas)
    print(f'Nota do trabalho: {nota1} + nota da prova: {nota2} - Sua média é: {media}')
    

    if media >= 7 :
        print(f'{aluno}, você foi aprovado')
    elif media > 4 or media < 6:
        print(f'{aluno}, você está em recuperação')
    else: 
        print(f'{aluno}, você está reprovado!')


    

