lista = [1,2,3,4,5]

#marca a quantidade de elementos da lista
fim = 5

while fim > 1:
    troca = False
    x = 0 #indice

    while x < (fim - 1):
        if lista[x] < lista[x +1]: #comparação para inverter em crescente ou descrescente > ou <
            troca =True
            temporario = lista[x]
            lista[x] = lista[x +1]
            lista[x + 1] = temporario
        x += 1
    if not troca:
        break
    fim -= 1
for i in lista:
    print(i)