from app.dao.dao import DAO
from app.models.usuario import Usuario


class Usuario_DAO:
    def __init__(self, database):
        self._database = database

    def save(self, usuario):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql =   """
                INSERT INTO USUARIO
                (NOME, EMAIL, DATA_NASCIMENTO)
                VALUES (%s, %s, %s)
                """
        cursor.execute(sql, (
            usuario.nome,
            usuario.email,
            usuario.data_nascimento
        ))
        conexao.commit()
        usuario.id = cursor.lastrowid
        self._database.desconectar(cursor, conexao)
        return usuario

    def get_all(self):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql =   """
                SELECT
                    ID,
                    NOME,
                    EMAIL,
                    DATA_NASCIMENTO
                FROM
                    USUARIO
                ORDER BY
                    NOME
                """
        cursor.execute(sql)
        registros = cursor.fetchall()
        usuarios = []
        for registro in registros:
            usuarios.append(
                Usuario(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3]
                )
            )
        self._database.desconectar(cursor, conexao)
        return usuarios

    def get_by_id(self, id):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql =   """
                SELECT
                    ID,
                    NOME,
                    EMAIL,
                    DATA_NASCIMENTO
                FROM 
                    USUARIO
                WHERE
                    ID = %s
                """
        cursor.execute(sql, (id,))
        registro = cursor.fetchone()
        self._database.desconectar(cursor, conexao)