import sqlite3
from bottle import route,run, template, request
import mako


USER_INFO = ['','','']

# Definimos rutas para manejar las plantillas (return index)
@route('/')
def index():
    
    if USER_INFO[0] == 'admin':
        admin = 1
    else:
        admin = 0

    return template('index', count = 0, admin = admin, user = USER_INFO)

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
        
        
        query = query + " except SELECT nombre,categoria,departamento,correo from usuarios WHERE nombre='admin';"
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

    
    if USER_INFO[0] == 'admin':
        admin = 1
    else:
        admin = 0
    
    return template('index', count = 1, resultado = result, admin = admin, user = USER_INFO )

# Identificacion de usuarios.  (return login)

@route('/login', method = 'GET')
def login():
    return template('login', count = 0, error = '')

@route('/login_done', method='POST')
def do_login():
    
    try:
        correo = request.forms.get('mail')
        password = request.forms.get('password')

        conn = sqlite3.connect('bottle.db')
        c = conn.cursor()
        query = "SELECT nombre,correo,pass FROM usuarios WHERE 1=1"

        if (correo != 'None'):
            query = query + " and correo = '{}' ".format(correo)    

        if (password != ''):
            query = query + " and pass = '{}' ".format(password)

        query = query + ";"
        print('\n'+query+'\n')
        c.execute(query)
        result = c.fetchall()
        c.close()

        result = list(result[0])

        if result[0] == 'admin':
            ADMIN = True
            USER_INFO[0] = result[0]
            USER_INFO[1] = result[1]
            USER_INFO[2] = result[2]
        else:
            USER = True
            USER_INFO[0] = result[0]
            USER_INFO[1] = result[1]
            USER_INFO[2] = result[1]

    except sqlite3.Error as error:
        print("Error en la consulta",error)

    except IndexError:
        return template('login', count = 0, error = 'Error al Introducir los datos')

    finally:
        if (conn):
            conn.close()
            print("Conexion Cerrada")

    return template('login', count = 1, error = '')

# Registro de Usuarios. (return register)

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



# INICIALIZACIÓN DE EL SERVIDOR


if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)