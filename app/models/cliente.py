class Cliente:

    def __init__(self, id, nome, email, data_nascimento, limite_credito):
        self._id = id
        self._nome = nome
        self._email = email
        self._data_nascimento = data_nascimento
        self._limite_credito = limite_credito

    def atualizar_dados(self, novo_nome, nova_data_nascimento, novo_limite_credito):
        self._nome = novo_nome
        self._data_nascimento = nova_data_nascimento
        self._limite_credito = novo_limite_credito

    
    def validar_limite_credito(self, limite_credito):
        if limite_credito < 0:
            raise ValueError("O limite de crédito não pode ser negativo.") # Ajustado: ValueError