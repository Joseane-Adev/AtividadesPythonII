import json
from pathlib import Path

caminho = Path('nota_aluno.json')
if caminho.exists():
    with caminho.open('r', encoding='utf-8') as arquivo:
        lista_aluno = json.load(arquivo)
else:
    lista_aluno = {} 

print('Aperte enter para sair do programa!')
while aluno := input('Digite seu nome: '):
    notas = input('Digite quatro notas separadas por espaço: ')
    notas = [float(n) for n in notas.split()]
    lista_aluno[aluno] = notas
    media = sum(notas) / len(notas)
    print(f'Média do aluno: {media:.2f}')

#gravar
with Path('nota_aluno.json').open('w',encoding='utf-8') as arquivo_notas:
    json.dump(lista_aluno,arquivo_notas, indent=2)



