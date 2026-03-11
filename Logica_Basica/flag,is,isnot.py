v1 = 10
print(id(v1))

'''
flag - marcar um local
none = noa valor
is= é
is not = nao é
id = identidade

'''
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('NÃO FAÇA ALGO')

print(passou_no_if, passou_no_if is None)
#passou no if (True), passou no if é None = False
print(passou_no_if, passou_no_if is not None)
#passou no if (True), passou no if não é None = (True)