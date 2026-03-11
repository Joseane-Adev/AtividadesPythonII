
hora = int(input('Digite somente a hora do dia: '))

if (hora >= 6) and  (hora <= 11):
    print('Bom dia')
elif (hora >=12) and (hora<= 17 ):
    print('Boa tarde!')
else:
   print('Boa noite')

#outra forma
'''
try:
    hora = int(input('Digite somente a hora do dia: '))

    if (hora >= 6) and  (hora <= 11):
        print('Bom dia')
    elif (hora >=12) and (hora<= 17 ):
        print('Boa tarde!')
    else:
       print('Boa noite')
except:
    print('Por favor, digite um número inteiro válido.')


'''