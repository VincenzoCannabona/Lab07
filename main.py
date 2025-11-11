import flet as ft

from UI import controller
from model.model import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()
    my_controller.carica_musei()        #popolo la dropdown
    my_controller.carica_epoca()



ft.app(target=main)
