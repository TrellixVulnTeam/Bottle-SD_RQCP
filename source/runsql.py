# runsql.py

import sqlite3

def databasecreate():

    """
    Función que se encarga de crear en un primer lugar una base de datos para poder crear
    el esquema de las tablas en la APIRest. Esta se encarga simplemente de facilitar la
    creación de la Base de Datos *Padre* sobre la cual poder introducir más información

        :param name: conn
                    Objeto de sql que se encarga de realizar todas las operaciones con la Base de Datos sqlite3.
    """

    print("Creando la base de datos");

    conn = sqlite3.connect('bottle.db')
    conn.execute("CREATE TABLE usuarios (nombre char(50) PRIMARY KEY NOT NULL, dni char(10) NOT NULL, pass char(20) NOT NULL, correo char(60) NOT NULL, departamento char(100), categoria char(5))")
    conn.execute("INSERT INTO usuarios (nombre, dni, correo, departamento, categoria, pass) VALUES ('admin','admin','admin@uca.es','Administracion','ADM', 'admin') ")
    conn.commit()
    conn.close()
    print("\n Base de datos creada")    


if __name__ == '__main__':

    databasecreate()