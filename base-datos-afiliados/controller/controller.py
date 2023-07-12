from models.afiliado import Afiliado
from models.grupo_familiar import GrupoFamiliar
from view.main_window import MainWindow

class Controller:
    def __init__(self):
        self.view = MainWindow(self)

    def main(self):
        self.view.main()

    def crear_afiliado(self, nombre, apellido, dni, nro_afiliado, cantidad_familiares):
        afiliado = Afiliado(nombre, apellido, dni, nro_afiliado, cantidad_familiares)
        afiliado.guardar()

    def agregar_familiar(self, afiliado_id, nombre, apellido, dni, nro_afiliado):
        familiar = GrupoFamiliar(afiliado_id, nombre, apellido, dni, nro_afiliado)
        familiar.guardar()

    def obtener_afiliados(self):
        return Afiliado.get_all()