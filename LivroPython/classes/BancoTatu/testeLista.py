from lista2_unica import ListaUnica

lu = ListaUnica(int)
lu.append(5)
lu.append(3)
#lu.adiciona(2.5)



lu.append(5)
lu.append(7)
for x in lu:
    print(x)

#trocar
lu[0] = 10
print(lu)