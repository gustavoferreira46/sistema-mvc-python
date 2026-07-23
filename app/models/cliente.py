from app.core.data_utils import Data_Utils

class Cliente:

    def __init__(self, id, nome, email, data_nascimento, limite_credito, cidade:Cidade):
        self._id = id
        self._nome = nome
        self._email = email
        self._data_nascimento = data_nascimento
        self._limite_credito = limite_credito
        self._cidade = cidade

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data_nascimento):
        self._data_nascimento = nova_data_nascimento

    @property
    def limite_credito(self):
        return self._limite_credito

    @limite_credito.setter
    def limite_credito(self, novo_limite_credito):
        self._limite_credito = novo_limite_credito

    @property
    def idade(self):
        return Data_Utils.calcular_idade(self._data_nascimento)
    
    @property
    def cidade(self):
        return self._cidade 
    
    @Cidade.setter
    def fornecedor(self, nova_cidade):
        self._cidade = nova_cidade


    def atualizar_dados(self, novo_nome, nova_data_nascimento, novo_limite_credito):
        self._nome = novo_nome
        self._data_nascimento = nova_data_nascimento
        self._limite_credito = novo_limite_credito
        self._cidade = nova_cidade

    def validar_limite_credito(self, limite_credito):
        if limite_credito < 0:
            raise ValueError("O limite de crédito não pode ser negativo.")