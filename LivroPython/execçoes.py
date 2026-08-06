class NovaException(Exception):
    pass

def lançador():
    raise NovaException

try:
    lançador()
except NovaException:
    print('Uma exeção do tipo NovaException foi lançada')
    