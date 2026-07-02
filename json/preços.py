import json
from pathlib import Path

tabela_precos = {}
print('CRiando tabela de preços')


while produto := input('Digite o produto: '):
    preco = input('Digite o preço: ')
    tabela_precos[produto] = preco

with Path('precos.json').open('w', encoding='utf-8') as arquivo:
    json.dump(tabela_precos, arquivo,indent=2, ensure_ascii=False)

