import time

agora = time.localtime()

print(f'Ano: {agora.tm_year}')
print(f'Mês {agora.tm_mon}')
print(f'Dia: {agora.tm_mday}')
print(f'Hora: {agora.tm_hour}')


#formatando em string
                    #diasemana dia/mes/ano hora/minutos , variavel de tempo
print(time.strftime('%a %d/%m/%y %H:%M', agora))
print(time.strftime('Hoje é o %j dia do ano de %Y', agora))