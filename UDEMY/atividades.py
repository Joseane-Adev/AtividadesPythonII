#aumentar os produtos em 10%
#gere novos produtos por deep copy
import copy
from dados import produtos

novos_produtos = [
    #list comprehension
    {**p, 'preco': round(p['preco'] * 1.1, 2)} for p in copy.deepcopy(produtos)
]


#ordene os produtos por nome descrescente
#gerear produtos ordenados

produtos_ordenados = sorted(
    copy.deepcopy(produtos),
    key= lambda p: p['nome'],
    reverse= True #reverter os produtos do maior para menor
)
print(*produtos, sep='n')
print()
print(*produtos_ordenados, sep='\n')

produtos_ordenados_preco = sorted(
    copy.deepcopy(produtos),
    key= lambda p: p['preco']
)

print(*produtos, sep='n')
print()
print(*produtos_ordenados_preco, sep='\n')

    