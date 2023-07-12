import sqlite3

class GrupoFamiliar:
    def __init__(self, afiliado_id, nombre, apellido, dni, nro_afiliado):
        self.afiliado_id = afiliado_id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.nro_afiliado = nro_afiliado

    def guardar(self):
        #Conectamos a la BBDD
        conexion = sqlite3.connect("sindicato.db")
        cursor = conexion.cursor()
        #Guardamos el afiliado
        cursor.execute('''INSERT INTO afiliado (afiliado_id, nombre, apellido, dni, nro_afiliado) VALUES (?, ?, ?, ?, ?)''', (self.afiliado_id, self.nombre, self.apellido, self.dni, self.nro_afiliado))
        #Guardamos y cerramos
        conexion.commit()
        conexion.close()