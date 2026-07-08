class cliente_view:
    # CORRIGIDO: Agora recebe a lista de clientes e faz um loop por ela
    def mostrar_cliente(self, lista_de_clientes):
        print("\n--- Lista de Clientes ---")
        
        for cliente in lista_de_clientes:
            print(f"ID: {cliente._id}") # Corrigido para ._id
            print(f"Usuário: {cliente._nome}")
            print(f"Email: {cliente._email}")
            print(f"Data de Nascimento: {cliente._data_nascimento}")
            print(f"Limite de Crédito: R$ {cliente._limite_credito:.2f}")
            print("-" * 25)