import os
import sys

diretorio = input('Digite o nome do diretorio: ')
with open('imagens.html', 'w', encoding='utf-8') as pagina:
    pagina.write(
        '''
<DOCTYPE html>
<html lang=pt-BR>
<head>
<meta charset= 'utf-8'>
<title>pagina imagens</title>
</head>
<body>
<ul>
'''
)
    for imagens in os.listdir(diretorio):
            if imagens.lower().endswith(('.png', '.jpg')):
                pagina.write(f'<li><a href="{imagens}">{imagens}</a> </li>\n')
            
    
           
    pagina.write('''
</ul>
</body>
</html>''')