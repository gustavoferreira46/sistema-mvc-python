from model.usuario import Usuario
from dao.usuario_dao import usuario_dao


class usuarioController:
    def __init__(self):
        self.dao = usuario_dao()

    def criar_usuario(self, id, nome, email, data_nascimento):
        usuario = Usuario (id, nome, email, data_nascimento)
        self.dao.adicionar_usuario(usuario)
    
    def listar_usuarios(self):
        return self.dao.listar_usuarios()
    
    
   