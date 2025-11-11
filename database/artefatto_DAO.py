from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    @staticmethod
    def read_all_epoche():
        result = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT epoca
                 FROM artefatto"""
        cursor.execute(query, )
        result.append("Nessun filtro")
        for row in cursor:
            epoca = row['epoca']
            result.append(epoca)
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def read_artefatti_filtrati(museo, epoca):
        result = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    FROM artefatto
                    WHERE epoca = %s AND id_museo = %s"""
        cursor.execute(query, (epoca, museo) )
        for row in cursor:
            artefatto = Artefatto(row["id"], row["nome"], row["tipologia"],row["epoca"],row["id_museo"])
            result.append(artefatto)
        cursor.close()
        cnx.close()
        return result
