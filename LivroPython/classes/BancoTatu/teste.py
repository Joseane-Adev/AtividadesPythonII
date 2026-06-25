#importar da classe clientes
from clientes import Cliente
from bancos import Banco
from contas import Conta, ContaEspecial


#instancias da classe cliente
marcos = Cliente('Marcos da Silva', '777-1234')
ane = Cliente('Ane Alves','999-1235')
antonio = Cliente('Antônio Nobrega','555-666')
conta_dupla = Conta([marcos], '991-111')
banco = Banco('Money')
banco.abre_conta(ane)
conta_dupla.deposito(500)
#banco.lista_contas()


#somente uma conta
conta1= ContaEspecial([ane],numero='10' ,saldo=1000, limite=1000)
#(cliente, numero, deposito inicial)
conta1.saque(200)
conta1.extrato()

'''
#uma conta com duas pessoas
conta_conjunta = Conta([antonio, marcos], 3, 500)
conta_conjunta.resumo()
conta_conjunta.extrato()
'''
'''
print(f'Nome do cliente: {marcos.nome}, Telefone: {marcos.telefone}')
#print(f'Nome do cliente: {maria.nome}, Telefone: {maria.telefone}')

print(conta.resumo())

print(f'Deposito: {conta.deposito(100)}')
print(conta.resumo())

print(f'Saque: {conta.saque(40)}')
print(conta.resumo())
'''
