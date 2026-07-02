import datetime
from datetime import datetime

#imprime a data atual e a hora
data = datetime.datetime.now()

#imprime a hora exata com os segundos
dataHora = datetime.datetime.now().time()
print(dataHora)

#dia
dia = datetime.datetime.now()
print(f'Dia: {data.day}')
#mês
print(f'Mês: {data.month}')
#ano
print(f'Ano: {data.year}')


data1  =data.date() #mostra a data
print(data1)

##acessar hora,min e segundos
tempo = data.time()#hora completa
print(tempo)
#só hora
print(tempo.hour)
#só minu
print(tempo.minute)
#só segundos
print(tempo.second)
#microseconds
print(tempo.microsecond)
#dia da semana
print(tempo.fromisoformat('2026-07-01:18:49'))