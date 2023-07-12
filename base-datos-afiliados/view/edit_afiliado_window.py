import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class EditAfiliadoWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.title("Modificar Afiliado")
        self.controller = controller