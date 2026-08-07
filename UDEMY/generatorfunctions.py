#generator function - funçoes que sabe pausar
def generator(n=0, maximum=10):
    while True:

        yield n # pausar
        n += 1
        if n >= maximum:
            return


        
    #return 'acabou' #stopiteration
'''
gen = generator(n=5, maximum=8)
for x in gen:
    print(x)'''

#yield from

def gen1():
    yield 1
    yield 2

def gen2(gen):
    yield from gen
    yield 3
    yield 4

g = gen2(gen1())
for n in g:
    print(n)





