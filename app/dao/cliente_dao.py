class Cliente_DAO:
    def __init__(self):
        self.cliente = []
        
    def adicionar_cliente(self, cliente):
        self.cliente.append(cliente)

    def listar_clientes(self):
        return self.cliente        