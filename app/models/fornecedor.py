# ==========================
# MODEL
# ==========================
# O Model representa os dados do sistema.
# Ele guarda as informações do fornecedor
# e também contém as regras de negócio.

class Fornecedor:

    # Método construtor.
    # É executado quando criamos um novo fornecedor.
    def __init__(self, id, razao_social, nome_fantasia, cnpj, sla_atendimento):

        # Atributos do fornecedor
        self._id = id
        self._razao_social = razao_social
        self._nome_fantasia = nome_fantasia
        self._cnpj = cnpj
        self._sla_atendimento = sla_atendimento

        @property
        def id(self):
            return self._id
        
        @id.setter
        def id(self, novo_id):
            self._id = novo_id

        @property
        def razao_social(self):
            return self._razao_social
        
        @razao_social.setter
        def razao_social(self, nova_razao_social):
            self._razao_social = nova_razao_social

        @property
        def nome_fantasia(self, novo_nome_fantasia):
            return self._nome_fantasia
        
        @nome_fantasia.setter
        def nome_fantasia(self, novo_nome_fantasia):
            self._nome_fantasia = novo_nome_fantasia

        @property 
        def cnpj(self, novo_cnpj):
            return self._cnpj
        
        @cnpj.setter
        def cnpj(self, novo_cnpj):
            self._cnpj = novo_cnpj

        @property    
        def sla_atendimento(self, novo_sla):
            return self._sla_atendimento
        
        @sla_atendimento.setter
        def sla_atendimento(self, novo_sla):
            self._sla_atendimento = novo_sla


    # Regra de negócio.
    # Verifica se o SLA informado é válido.
    def validar_sla(self, sla):

        if sla < 0:
            raise ValueError(
                "O SLA de atendimento não pode ser negativo."
            )


    # Atualiza os dados do fornecedor.
    # Antes de atualizar, chama a validação.
    def atualizar_dados(
        self,
        nova_razao_social,
        novo_nome_fantasia,
        novo_cnpj,
        novo_sla
    ):

        # verifica se o SLA é válido
        self.validar_sla(novo_sla)

        # atualiza os atributos
        self._razao_social = nova_razao_social
        self._nome_fantasia = novo_nome_fantasia
        self._cnpj = novo_cnpj
        self._sla_atendimento = novo_sla