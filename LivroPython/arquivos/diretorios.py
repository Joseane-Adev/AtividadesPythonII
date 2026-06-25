import os
os.getcwd()
'''
#pasta a
os.chdir('a')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

#pasta b
os.chdir('b')
print(os.getcwd())

os.chdir('../c')
print(os.getcwd())
'''
#criar de uma só vez se não souber se tem diretorios intermediarios
#os.makedirs('avó/pai/filho')

#os.mkdir('velho')
#os.rename('velho', 'novodiretorio')

#apagar um diretorio
#os.rmdir('a')

#apagar um arquivo é remove

#listar arquivo e diretorio
#print(os.listdir('.'))
print(os.listdir('LivroPython/arquivos'))

