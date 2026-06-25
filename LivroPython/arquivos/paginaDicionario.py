filmes = {
    'drama': ['Cidadão Kane', 'O poderoso chefão'],
    'comedia': ['American Pie', 'Uma sexta-feira muito louca'],
    'guerra': ['Rambo', 'Os vingadores']
}

with open('filmes.html', 'w' , encoding='utf-8') as pagina:
    pagina.write(
    '''
<DOCTYPE html>
<html lang='pt-BR'>
<head>
<meta charset= utf-8>
<title>Filmes</title> 
</head>
<body>
''')

    
    for tema, titulo in filmes.items():
        pagina.write(f'<h2>{tema.capitalize()}</h2>\n')
        pagina.write(f'<ul>\n')
        for x in titulo:
            pagina.write(f'<li>{x}</li>\n')
        pagina.write('</ul>\n')
    pagina.write('</body></html>')