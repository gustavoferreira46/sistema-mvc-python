from controller.usuario_controller import usuarioController
from controller.cliente_controller import clienteController

from views.usuario_view import usuario_view
from views.cliente_view import cliente_view


usuario_controller = usuarioController()
cliente_controller = clienteController()

usuario_view_instancia = usuario_view() 
cliente_view_instancia = cliente_view()


usuario_controller.criar_usuario(
    1,
    "João Silva",
    "joaosilva@gmail.com",
    "25/07/1990"
)


cliente_controller.criar_cliente(
    1,
    "Maria Souza",
    "maria@gmail.com",  # Vírgula adicionada aqui
    "15/03/1985",
    1000.00
)


usuario_view_instancia.mostrar_usuario(usuario_controller.listar_usuarios())
cliente_view_instancia.mostrar_cliente(cliente_controller.listar_cliente())