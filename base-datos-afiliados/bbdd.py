import sqlite3
from controller.controller import Controller

#Conexión a la base de datos
conexion = sqlite3.connect("sindicato.db")
cursor = conexion.cursor()

#Crear tablas
cursor.execute('''CREATE TABLE IF NOT EXISTS afiliado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                dni TEXT,
                nro_afiliado TEXT,
                cantidad_familiares INTEGER
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS grupo_familiar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                afiliado_id INTEGER,
                nombre TEXT,
                apellido TEXT,
                dni TEXT,
                nro_afiliado TEXT,
                FOREIGN KEY (afiliado_id) REFERENCES afiliado (id)
)''')

#Guardamos cambios y cerramos conexion
conexion.commit()
conexion.close()

controller = Controller()

if __name__ == "__main__":
    controller.main()