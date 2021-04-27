import sqlite3

print("Creando la base de datos");

conn = sqlite3.connect('bottle.db')
conn.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre char(50), dni char(10), pass char(10), correo char(60), departamento char(100), categoria char(5))")
conn.execute("INSERT INTO usuarios (nombre, dni, correo, departamento, categoria, pass) VALUES ('admin','admin','admin@uca.es','Administracion','ADM', 'admin') ")
conn.execute("INSERT INTO usuarios (nombre, dni, correo, departamento, categoria, pass) VALUES ('Manolito Gonzalez Pino','55345724O','manolitogonzalez@uca.es','Departamento de Copmputacion','PAS', 'lamama') ")
conn.commit()

print("\n Base de datos creada")
