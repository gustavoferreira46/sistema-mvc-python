from app.dao.dao import DAO
from app.models.produto import Produto
class Produto_DAO(DAO):
    def __init__(self, database, fornecedor_dao):
        super().__init__(database)
        self._fornecedor_dao = fornecedor_dao

    def save(self, produto):
        conexao, cursor = self.conectar()
        try:
            sql = """
                INSERT INTO PRODUTO
                    (NOME, ESTOQUE, PRECO)
                    VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (
                produto.nome,
                produto.estoque,
                produto.preco
            ))
            conexao.commit()
            produto.id = cursor.lastrowid
            self._database.desconectar(cursor, conexao)
            return produto
        except Exception as e:
            conexao.rollback()
            self._database.desconectar(cursor, conexao)
            raise e
        finally:
            self._database.desconectar(cursor, conexao)
    
    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    SELECT
                        ID,
                        NOME,
                        ESTOQUE,
                        PRECO
                    FROM
                        PRODUTO
                    ORDER BY 
                        NOME
            """
            cursor.execute(sql)
            registros = cursor.fetchall()
            produtos = []
            for registro in registros:
                produtos.append(
                    Produto(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3]
                    )
                )
            self._database.desconectar(cursor, conexao)
            return produtos
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                SELECT
                    ID,
                    NOME,
                    ESTOQUE,
                    PRECO
                FROM
                    PRODUTO
                WHERE
                    ID = %s
                    """
            
            cursor.execute(sql,(id,))
            registro = cursor.fetchone()
            self._database.desconectar(cursor, conexao)
            if registro is None:
                return None
            return Produto(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
            )
        except Exception as e:
            raise e
        finally:
            self.desconectar(cursor, conexao)

    def update(self, produto):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE PRODUTO SET 
                            NOME = %s,
                            ESTOQUE = %s,
                            PRECO = %s
                        WHERE 
                            ID = %s
                    """
            cursor.execute(sql,(    
                                
                produto.nome,
                produto.estoque,
                produto.preco,
                produto.id
            ))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            self._database.desconectar(cursor, conexao)
            return sucesso
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)
        
    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        DELETE FROM PRODUTO  
                            WHERE 
                            ID = %s
                    """
            cursor.execute(sql,(id,))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            self._database.desconectar(cursor, conexao)
            return sucesso
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)


       
