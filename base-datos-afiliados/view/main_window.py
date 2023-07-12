import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from view.add_afiliado_window import AddAfiliadoWindow

class MainWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Sindicato Regional de Luz y Fuerza - Gestión de Afiliados")
        self.controller = controller
        self.boton_agregar = ttk.Button(self, text = "Agregar Afiliado", command = self.mostrar_agregar_afiliado)
        self.boton_agregar.pack()
        self.centrar_ventana()

    def main(self):
        self.mainloop()

    def mostrar_agregar_afiliado(self):
        add_afiliado_window = AddAfiliadoWindow(self)
        add_afiliado_window.grab_set()

    def mostrar_modificar_afiliado(self):
        edit_afiliado_window = EditAfiliadoWindow(self)
        edit_afiliado_window.grab_set()

    def centrar_ventana(self):
        self.update()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - ancho) // 2
        y_offset = (self.winfo_screenheight() - alto) // 2
        self.geometry(f"{ancho}x{alto}+{x_offset}+{y_offset}")
    
