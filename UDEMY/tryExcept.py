#try, excepty, selse e finally
'''
try:
    a = 18
    b= 0
    print(b[0])
    c = a / b
except ZeroDivisionError:
    print('Não é possível dividir')
except NameError:
    print(('Nome não foi definido'))
except (TypeError, IndexError) as error:
    print('TypeERROR + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')


'''
'''
try:
    print(1)

except ZeroDivisionError:
    print('dividiu')
else:
    print('não deu erro')
#sempre será executado o finally, não trata execçoes
finally:
    print(2)
'''
#raise lançando exceções
print(123)
raise ValueError('Deu erro')
print(456)









