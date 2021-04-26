import sqlite3
from bottle import route,run, template, request
import mako

# Definimos rutas para manejar las plantillas
@route('/')
def index():
    return template('index', count = 0, admin = 0)

@route('/identificado', method='GET')
def identified():

    # if user = usuario normal , admin = 0 
    # else admin = 1

    return template('index')

# Identificacion de usuarios.

@route('/login', method = 'GET')
def login():
    return template('login', count = 0)

@route('/login_done', method='POST')
def do_login():
    correo = request.forms.get('username')
    password = request.forms.get('password')
    return template('login', count = 1)

# Registro de Usuarios.

@route('/register', method = 'GET')
def register():
    return template('register', count = 0)

@route('/register_done', method='POST')
def do_register():
    try:
            name = request.forms.get('name')
            password = request.forms.get('password')
            correo = request.forms.get('mail')
            dni = request.forms.get('dni')
            departamento = request.forms.get('departamento')
            categoria = request.forms.get('categoria')

            print(departamento)
            print(categoria)

            conn = sqlite3.connect('bottle.db')
            c = conn.cursor()
            command = "INSERT INTO usuarios (nombre,dni,correo,departamento,categoria,pass) VALUES ('{}' , '{}' , '{}' , '{}' , '{}' , '{}');".format(
                name, dni, correo, departamento, categoria, password)
            c.execute(command)
            conn.commit()
            c.close()

    except sqlite3.Error as error:
            print("Error mientras se insertaban los datos",error)

    finally:
            if (conn):
                conn.close()
                print("Conexion Cerrada")
    
    return template('register', count = 1)

@route('/search_done', method='POST')
def search_done():
    try:
        username = request.forms.get('username')
        departamento = request.forms.get('departamento')
        categoria = request.forms.get('categoria')

        conn = sqlite3.connect('bottle.db')
        c = conn.cursor()
        
        query = "SELECT nombre,categoria,departamento,correo FROM usuarios WHERE 1=1"

        if (username != ''):
            query = query + " and nombre like '%{}%' ".format(username)

        if (categoria != '1'):
            query = query + " and categoria = '{}' ".format(categoria)

        if (departamento != '1'):
            query = query + " and departamento = '{}' ".format(departamento)
        
        
        query = query + ";"
        print('\n'+query+'\n')
        c.execute(query)
        result = c.fetchall()
        c.close()

    except sqlite3.Error as error:
        print("Error mientras se insertaban los datos",error)

    finally:
        if (conn):
            conn.close()
            print("Conexion Cerrada")

    return template('index', count = 1, resultado = result)


if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)