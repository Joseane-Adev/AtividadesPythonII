
'''ligado = False
canal = 2

def liga_TV():
    global ligado
    ligado = True

def desliga_TV():
    global ligado
    ligado = False
'''

tv = {'ligado': False, 'canal': 2}

tv_sala = {'ligado': False, 'canal': 2}
tv_quarto = {'ligado': True, 'canal': 4}

def liga_tv(tv):
    #pega o dicionario, a primeira chave e ativa True
    tv['ligado'] = True

def desliga_tv(tv):
    tv['ligado'] = False

liga_tv(tv_sala)
desliga_tv(tv_quarto)

