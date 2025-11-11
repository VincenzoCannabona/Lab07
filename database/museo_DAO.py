from database import DB_connect
from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    @staticmethod
    def read_all_museums():
        result = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection error")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT id,nome 
                        FROM museo"""
            cursor.execute(query,)
            result.append({"id": 0, "nome": "Nessun filtro"})
            for row in cursor:
                museo = {"id": row["id"], "nome": row["nome"]}
                result.append(museo)
            cursor.close()
            cnx.close()
            return result
