class usuario_view:

    def mostrar_usuario(self, lista_de_usuarios):
        print("\n--- Lista de Usuários ---")
        
        
        for usuario in lista_de_usuarios:
            
            print(f"ID: {usuario._id}")
            print(f"Nome: {usuario._nome}")
            print(f"Email:")
            print(f"{usuario._email}")
            
        print("-------------------------\n")