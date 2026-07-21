class Usuario_Terminal_View:

    def renderizar_menu(self):
        print("\n=== GERENCIAR USUÁRIOS ===")
        print("1 - Cadastrar Usuário")
        print("0 - Voltar")
        print("=" * 30)
        opcao = input("Escolha uma opção: ")
        return int(opcao)

    def ler_dados_usuario(self):
        nome = input("Nome: ")
        email = input("Email: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        return nome, email, data_nascimento

    def exibir_mensagem(self, mensagem, sucesso=True):
        print(mensagem)

    def mostrar_usuario(self, lista_de_usuarios):
        print("\n--- Lista de Usuários ---")

        for usuario in lista_de_usuarios:
            print(f"ID: {usuario._id}")
            print(f"Nome: {usuario._nome}")
            print(f"Email:")
            print(f"{usuario._email}")

        print("-------------------------\n")