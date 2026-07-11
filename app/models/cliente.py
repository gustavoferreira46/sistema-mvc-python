from app.core.data_utils import Data_Utils

class Cliente:

    def __init__(self, id, nome, email, data_nascimento, limite_credito):
        self._id = id
        self._nome = nome
        self._email = email
        self._data_nascimento = data_nascimento
        self._limite_credito = limite_credito

        
        @property
        def nome(self, nome):
            return self._nome
        
        @nome.setter
        def nome (self, novo_nome):
            self._nome = novo_nome

        @property
        def data_nascimento (self, data_nascimnento):
            return self._data_nascimento
        
        @data_nascimento.setter
        def data_nascimento (self, nova_data_nascimento):
            self._data_nascimento = nova_data_nascimento

        @property
        def limite_credito (self, novo_limite_credito):
            return self._limite_credito
        
        @limite_credito.setter
        def limite_credito (self, novo_limite_credito):
            self._limite_credito = novo_limite_credito

        @property
        def idade(self):
            return Data_Utils.calcular_idade(self._data_nascimento)

    def atualizar_dados(self, novo_nome, nova_data_nascimento, novo_limite_credito):
        self._nome = novo_nome
        self._data_nascimento = nova_data_nascimento
        self._limite_credito = novo_limite_credito

    
    def validar_limite_credito(self, limite_credito):
        if limite_credito < 0:
            raise ValueError("O limite de crédito não pode ser negativo.") # Ajustado: ValueError