import os 
import sys
for raiz, diretorios, arquivos in os.walk(sys.argv[0]):
    print('\nCaminho', raiz)
    for dir in diretorios:
        print(f' {dir}')
    for arq in arquivos:
        print(f'{arq}')
    print(f'{len(diretorios)} diretorio(s), {len(arquivos)} arquivo(s)')