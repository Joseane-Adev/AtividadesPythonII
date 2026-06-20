with open('pagina.html', 'w', encoding='utf-8') as pagina:
    pagina.write('''
        <!DOCTYPE html>
        <html lang=\'pt-BR\'>
        <head>
        <meta charset=\'utf-8\'>
        <title>Titulo da página</title>
        </head>
        <body>
        'OLá''')
    for linha in range(10):
        pagina.write(f'<p>{linha}<p>\n')
    pagina.write('''
        </body>
        </html>''')