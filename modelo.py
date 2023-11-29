import sqlite3
from datetime import date


class BlogModel:
    def __init__(
        self,
    ):
        # Creo la conexion con la base de datos
        self.con = sqlite3.connect("blog.db")
        self.cursor = self.con.cursor()
        # Creo las instrucciones para la tabla
        sql_table = "CREATE TABLE IF NOT EXISTS blogs (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL, email TEXT NOT NULL, created_date TEXT NOT NULL)"
        # Ejecuto la tabla
        self.cursor.execute(sql_table)
        # confirmo ejecucion
        self.con.commit()

    # Funcion de alta
    def alta(self, title, content, email):
        # Defino instruciones de datos
        current_date = str(date.today())
        data = (title, content, email, current_date)
        sql = (
            "INSERT INTO blogs(title, content, email, created_date) VALUES(?, ?, ?, ?)"
        )
        self.cursor.execute(sql, data)
        self.con.commit()

    # Funcion modificar
    def modificar(self, id, title, content, email):
        # Defino instruciones de datos
        data = (title, content, email, id)
        sql = "UPDATE blogs SET title = ?, content = ?, email = ? WHERE id = ?"
        # ejecuto y confirmo
        self.cursor.execute(sql, data)
        self.con.commit()

    # Funcion borrar
    def borrar(self, mi_id):
        # defino instrucciones
        sql = "DELETE FROM blogs WHERE id = ?"
        data = (mi_id,)
        # ejecuto y confirmo
        self.cursor.execute(sql, data)
        self.con.commit()

    # Funcion consultar
    def consultar(self):
        # Defino las instruciones
        sql = "SELECT * FROM blogs ORDER BY id ASC"
        # Ejecuto
        datos = self.cursor.execute(sql)
        # Devuelvo los datos
        return datos.fetchall()

    def close_conection(self):
        # termino conexion
        self.con.close()
