import sqlite3
class Afiliado:
    def __init__(self, nombre, apellido, dni, nro_afiliado, cantidad_familiares):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.nro_afiliado = nro_afiliado
        self.cantidad_familiares = cantidad_familiares

    def guardar(self):
        #Conectamos a la BBDD
        conexion = sqlite3.connect("sindicato.db")
        cursor = conexion.cursor()
        #Guardamos el afiliado
        cursor.execute('''INSERT INTO afiliado (nombre, apellido, dni, nro_afiliado, cantidad_familiares) VALUES (?, ?, ?, ?, ?)''', (self.nombre, self.apellido, self.dni, self.nro_afiliado, self.cantidad_familiares))
        #Guardamos y cerramos
        conexion.commit()
        conexion.close()

    @staticmethod
    def get_all():
        conexion = sqlite3.connect("sindicato.db")
        cursor = conexion.cursor()
        #Seleccionamos todo de la tabla afiliados
        cursor.execute("SELECT * FROM afiliado")
        #Guardamos los datos en una lista
        afiliados = cursor.fetchall()
        conexion.close()
        return afiliados