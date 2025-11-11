from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        artefatti_filtrati= ArtefattoDAO.read_artefatti_filtrati(museo, epoca)
        return artefatti_filtrati

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        epoche = ArtefattoDAO.read_all_epoche()
        return epoche

    # --- MUSEI ---
    def get_museums(self):
        """ Restituisce la lista di tutti i musei."""
        musei = MuseoDAO.read_all_museums()
        return musei

