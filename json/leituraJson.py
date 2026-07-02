import json
from pathlib import Path

#mostrar o diretorio
caminho = Path('lista.json').resolve()

#atribuir o caminho
diretorio = Path(r'C:\Users\Usuário\Desktop\PythonUDEEMY-LIVRO\json\lista.json')

with diretorio.open(encoding='utf-8') as arquivo:
    turma = json.load(arquivo)
for aluno in turma:
    print('Nome: ' , aluno['nome'])
    print('Notas: ', aluno['notas'])
    print('Media: ', sum(aluno['notas']) / len(aluno['notas']))
    #soma as notas da lista e depois divide pela qtd de notas
    print()
