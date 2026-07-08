class cliente_dao:
    def __init__(self):
        self.cliente = []
        
    def adicionar_cliente(self, cliente):
        self.cliente.append(cliente)

    def listar_clientes(self):
        return self.cliente        