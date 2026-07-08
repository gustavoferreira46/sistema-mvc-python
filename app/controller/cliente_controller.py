from model.cliente import Cliente
from dao.cliente_dao import cliente_dao

class clienteController:
    def __init__(self):
        self.dao = cliente_dao()

    def criar_cliente(self, id, nome, email, data_nascimento, limite_credito):
        cliente = Cliente(id, nome, email, data_nascimento, limite_credito)
        self.dao.adicionar_cliente(cliente)
    
    # CORRIGIDO: Colocado para dentro da classe (com recuo de 4 espaços)
    def listar_cliente(self):
        return self.dao.listar_clientes()