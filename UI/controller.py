import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def carica_musei(self):
        musei= self._model.get_museums()
        self._view.dd_museo.options.clear()
        for m in musei:
            self._view.dd_museo.options.append(ft.dropdown.Option(text=m["nome"], key=m["id"]))

        self._view.dd_museo.update()


    def carica_epoca(self):
        epoche = self._model.get_epoche()
        self._view.dd_epoca.options.clear()
        for e in epoche:
            self._view.dd_epoca.options.append(ft.dropdown.Option(text=e))

        self._view.dd_epoca.update()

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti_filtrati(self, e):
        self.museo_selezionato =self._view.dd_museo.value
        self.epoca_selezionata = self._view.dd_epoca.value
        artefatti=self._model.get_artefatti_filtrati(self.museo_selezionato, self.epoca_selezionata)
        self._view.lista_artefatti_filtrati.controls.clear()
        for a in artefatti:
            self._view.lista_artefatti_filtrati.controls.append(ft.Text(f"{a.nome} ({a.epoca}) - {a.tipologia}"))
        self._view.lista_artefatti_filtrati.update()
        self._view.page.update()
