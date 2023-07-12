import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Sindicato Regional de Luz y Fuerza - Gestión de Afiliados")
        self.controller = controller
        #Creamos componentes
        self.label_nombre = ttk.Label(self, text = "Nombre")
        self.entry_nombre = ttk.Entry(self)
        self.label_apellido = ttk.Label(self, text = "Apellido")
        self.entry_apellido = ttk.Entry(self)        
        self.label_dni = ttk.Label(self, text = "DNI")
        self.entry_dni = ttk.Entry(self)
        self.label_nro_afiliado = ttk.Label(self, text = "N° Afiliado")
        self.entry_nro_afiliado = ttk.Entry(self)
        self.label_cantidad_familiares = ttk.Label(self, text = "Cantidad de Familiares")
        self.entry_cantidad_familiares = ttk.Entry(self)
        self.boton_confirmar = ttk.Button(self, text = "Confirmar", command = self.confirmar_datos)
        #Posicionamos componentes
        self.label_nombre.grid(row = 0, column = 0)
        self.entry_nombre.grid(row = 0, column = 1)
        self.label_apellido.grid(row = 1, column = 0)
        self.entry_apellido.grid(row = 1, column = 1)       
        self.label_dni.grid(row = 2, column = 0)
        self.entry_dni.grid(row = 2, column = 1)
        self.label_nro_afiliado.grid(row = 3, column = 0)
        self.entry_nro_afiliado.grid(row = 3, column = 1)
        self.label_cantidad_familiares.grid(row = 4, column = 0)
        self.entry_cantidad_familiares.grid(row = 4, column = 1)
        self.boton_confirmar.grid(row = 5, columnspan = 2)
        self.centrar_ventana()

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def mostrar_error(self, titulo, mensaje):
        messagebox.showerror(titulo, mensaje)

    def main(self):
        self.mainloop()

    def centrar_ventana(self):
        self.update()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - ancho) // 2
        y_offset = (self.winfo_screenheight() - alto) // 2
        self.geometry(f"{ancho}x{alto}+{x_offset}+{y_offset}")
    
    def confirmar_datos(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        dni = self.entry_dni.get()
        nro_afiliado = self.entry_nro_afiliado.get()
        cantidad_familiares = self.entry_cantidad_familiares.get()
        if nombre and apellido and dni and nro_afiliado and cantidad_familiares:
            self.controller.crear_afiliado(nombre, apellido, dni, nro_afiliado, cantidad_familiares)
            self.mostrar_mensaje("CONFIRMACION", "Los datos fueron registrados correctamente.")
        else:
            self.mostrar_error("ERROR" ,"Por favor, complete todos los campos.")
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.entry_dni.delete(0, tk.END)
        self.entry_nro_afiliado.delete(0, tk.END)
        self.entry_cantidad_familiares.delete(0, tk.END)
