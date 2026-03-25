a = set()

a.add(22)
print(a)
a.add(21)
a.add(-1)
print(a)

#para saber se o elemento já existe
21 in a

#criando uma nova set

b= ([4,5,6])
print(len(b))

#União de conjuntos
x = set(['a', 1, 'f'])
z = set([2,4])
novoset = set(['oi'])

x.union(z)
print(x)
uniao = x | novoset
print(uniao)

#intersecção

A = {1,2,3,6}
B = {2,4,5,6}
intersecion = A & B
inter = A.intersection(B)
print(intersecion, inter)

#Diferença

diferença = A - B
print(diferença)