# run.py
import sqlite3
from bottle import route,run, template, request
import mako

USER_INFO = ['','','']
USER_NAME = ['']
ASIG_LIST = []

@route('/')
def index():

    """
    Ruta que interpreta la pagina principal con algunas opciones modificables

    :param count:
                Selector de modos para el template index
    :param admin:
                Selector de modo admin para el template index
    :param user:
                Información relativa al usuario que proviene del login
    """
    
    try:
        correo = request.forms.get('mail')
        password = request.forms.get('password')

        conn = sqlite3.connect('bottle.db')
        c = conn.cursor()

        
        query = "SELECT nombre FROM asignatura WHERE 1=1;"
        print('\n'+query+'\n')
        
        c.execute(query)
        result = c.fetchall()
        c.close()       
        ASIG_LIST = result


    except sqlite3.Error as error:
        print("Error en la consulta",error)

    finally:
        if (conn):
            conn.close()
            print("Conexion Cerrada")

    if USER_INFO[0] == 'admin':
        admin = 1
    else:
        admin = 0

    return template('index', count = 0, admin = admin, user = USER_INFO , asignatura = result)


@route('/search_done', method='POST')
def search_done():
    
    """
    Ruta que interpreta el resultado del formulario de búsqueda y realiza una serie de acciones
    dependiendo de los campos introducidos durante la búsqueda.

    :param username:
                Cadena con el nombre introducido en el formulario
    :param departamento:
                Cadena con el departamento introducido en el formulario
    :param name: categoria
                Cadena con la categoria introducida en el formulario
    :param name: conn
                Objeto sql para realizar las conexiones a la base de datos estipulada
    :param name: c
                Cursos de la conexión sql
    :param query:
                query que se encarga de realizar la operacion adecuada para la consulta sql
    :param result:
                Resultado de la consulta sql
    :param error:
                Cadena con el contenido del error que se ha producido
    :param count:
                Selector de modos para el template register

    """

    try:
        username = request.forms.get('username')
        departamento = request.forms.get('departamento')
        categoria = request.forms.get('categoria')
        dni = request.forms.get('dni')
        asignatura = request.forms.get('asignatura')

        conn = sqlite3.connect('bottle.db')
        c = conn.cursor()
        
        query = "SELECT nombre,categoria,departamento,correo FROM usuarios WHERE 1=1"

        if (username != ''):
            query = query + " and nombre like '%{}%' ".format(username)
       
        if (dni != ''):
            query = query + " and dni like '{}' ".format(dni)
        
        if (categoria != '1'):
            query = query + " and categoria = '{}' ".format(categoria)

        if (departamento != '1'):
            query = query + " and departamento = '{}' ".format(departamento)
        
        query = query + " except SELECT nombre,categoria,departamento,correo from usuarios WHERE nombre='admin';"
        print('\n'+query+'\n')


        if (asignatura != '1'):
            
            query = "select nombre,categoria,departamento,correo FROM usuarios where nombre IN (select profesor from prof_asig where asignatura='{}');".format(asignatura)

        c.execute(query)
        result = c.fetchall()

        c.execute("SELECT nombre FROM asignatura WHERE 1=1;")
        ASIG_LIST = c.fetchall()
        
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
    
    return template('index', count = 1, asignatura = ASIG_LIST ,resultado = result, admin = admin, user = USER_INFO )


@route('/login', method = 'GET')
def login():

    """
    Ruta que nos lleva por primera vez al login

    :param count:
                    Selector de modos para el template login.
    :param error:
                    Cadena con el contenido del error que se ha producido durante el login
    """
    return template('login', count = 0, error = '')

@route('/login_done', method='POST')
def do_login():

    """
    Ruta que interpreta el resultado del formulario login y realiza una serie de acciones
    dependiendo de los campos introducidos durante el login. Devuelve tambien parte de 
    la información relativa al usuario introducido

    :param password:
                Cadena con la contraseña introducida en el formulario
    :param correo:
                Cadena con el correo introducido en el formulario
    :param conn:
                Objeto sql para realizar las conexiones a la base de datos estipulada
    :param c:
                Cursos de la conexión sql
    :param query:
                Query que se encarga de realizar la operacion adecuada para la consulta sql
    :param result:
                Resultado de la consulta sql
    :param error:
                Cadena con el contenido del error que se ha producido
    :param count:
                Selector de modos para el template register
    :global USER_INFO:
                Lista global que almacena la información relativa a un usuario tras su logeo.

    """
    
    try:
        correo = request.forms.get('mail')
        password = request.forms.get('password')

        conn = sqlite3.connect('bottle.db')
        c = conn.cursor()

        if (correo != 'None' and password != ''):
            query = "SELECT nombre,correo,pass FROM usuarios WHERE 1=1 and correo='{}' and pass = '{}';".format(correo,password)
            print('\n'+query+'\n')
        
        else:
            return template('login', count = 0, error = 'Error al introducir los datos')

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
        return template('login', count = 0, error = 'Error al introducir los datos')

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

    """
    Ruta que muestra el formulario del cuestionario
    
    :param count:
                Selector de modos para el template register
    
    """
    return template('register', count = 0, error = '')

@route('/register_done', method='POST')
def do_register():

    """
    Ruta que interpreta el resultado del formulario registro y realiza una serie de acciones
    dependiendo de los campos introducidos durante el registro

    :param name:
                Cadena con el nombre introducido en el formulario
    :param password:
                Cadena con la contraseña introducida en el formulario
    :param correo:
                Cadena con el correo introducido en el formulario
    :param dni:
                Cadena con el dni introducido en el formulario
    :param departamento:
                Cadena con el departamento introducido en el formulario
    :param categoria:
                Cadena con la categoria introducida en el formulario
    :param conn:
                Objeto sql para realizar las conexiones a la base de datos estipulada
    :param c:
                Cursos de la conexión sql
    :param command:
                Comando que se encarga de realizar la operacion adecuada para la consulta sql
    :param result:
                Resultado de la consulta sql
    :param error:
                Cadena con el contenido del error que se ha producido
    :param count:
                Selector de modos para el template register

    """
    try:
    
        name = request.forms.get('name')
        password = request.forms.get('password')
        correo = request.forms.get('mail')
        dni = request.forms.get('dni')
        departamento = request.forms.get('departamento')
        categoria = request.forms.get('categoria')
        asignatura = request.forms.getlist('asignatura')

        conn = sqlite3.connect('bottle.db')
        c = conn.cursor()

        print(name)
        print(correo)
        print(dni)
        print(departamento)

        if ((name != '' and name != 'admin' and name != None) and dni != '' and correo != '' and password != '' and categoria != '1' and departamento != '1'):

            command = "INSERT INTO usuarios (nombre,dni,correo,departamento,categoria,pass) VALUES ('{}' , '{}' , '{}' , '{}' , '{}' , '{}');".format(
            name, dni, correo, departamento, categoria, password)

            print("HOLA")
            USER_NAME[0] = name
            print(USER_NAME[0])
            c.execute(command)
            conn.commit()
            
            if (categoria == 'PDI'):
                c.execute("SELECT nombre FROM asignatura;")
                asignatura = c.fetchall()
                return template('register', count = 2, error = '', asignatura = asignatura)
            else:
                return template('register', count = 1, error = '')
        
        else:
            print(USER_NAME[0])
            if asignatura != None:
                for i in asignatura:
                    print("marca de base de datos")
                    command = "INSERT INTO prof_asig (profesor,asignatura) VALUES ('{}','{}')".format(USER_NAME[0], i)
                    c.execute(command)
                    conn.commit()
                return template("register", count = 1, error='')

            else:
                return template('register', count = 0 , error = 'Falta algun campo')
        
        c.close()

    except sqlite3.Error as m_error:
            print("Error mientras se insertaban los datos",m_error)
            return template('register', count = 0 , error = 'Error Base de Datos')


    finally:
            if (conn):
                conn.close()
                print("Conexion Cerrada")

@route('/modify')
def modify():

    """
    Ruta que solo se activa si eres admin y que sirve para modificar la información, excepto
    el nombre, de cualquier usuario, incluido el propio admin.

    :param conn:
                Objeto sql para realizar las conexiones a la base de datos estipulada
    :param c:
                Cursos de la conexión sql
    :param query:
                Query que se encarga de realizar la operacion adecuada para la consulta sql
    :param result:
                Resultado de la consulta sql
    :param error:
                Cadena con el contenido del error que se ha producido
    :param count:
                Selector de modos para el template register
    """



    try:


        conn = sqlite3.connect('bottle.db')
        c = conn.cursor()
        
        query = "SELECT nombre,dni FROM usuarios WHERE 1=1;"

        print('\n'+query+'\n')
        
        c.execute(query)
        result = c.fetchall()
        c.close()

    except sqlite3.Error as error:
        print("Error mientras se extraían los datos",error)

    finally:
        if (conn):
            conn.close()
            print("Conexion Cerrada")

    return template('modify', cont = 0 , consulta = result)

@route('/modify_done', method = 'POST')
def modify_done():

    """
    Ruta que aparece tras realizar la modificación de algun usuario por parte del administrador, 
    se encarga de manejar toda la información relativa al formulario rellenado a la hora 
    de modificar la información de cualquier usuario.

    :param name:
                Cadena con el nombre introducido en el formulario
    :param password:
                Cadena con la contraseña introducida en el formulario
    :param correo:
                Cadena con el correo introducido en el formulario
    :param dni:
                Cadena con el dni introducido en el formulario
    :param departamento:
                Cadena con el departamento introducido en el formulario
    :param categoria:
                Cadena con la categoria introducida en el formulario
    :param conn:
                Objeto sql para realizar las conexiones a la base de datos estipulada
    :param c:
                Cursos de la conexión sql
    :param query:
                Query que se encarga de realizar la operacion adecuada para la consulta sql
    :param result:
                Resultado de la consulta sql
    :param error:
                Cadena con el contenido del error que se ha producido
    :param cont:
                Selector de modos para el template register

    """


    try:
        name = request.forms.get('name')
        password = request.forms.get('password')
        correo = request.forms.get('mail')
        dni = request.forms.get('dni')
        departamento = request.forms.get('departamento')
        categoria = request.forms.get('categoria')

        conn = sqlite3.connect('bottle.db')
        c = conn.cursor()

        query = "UPDATE usuarios SET dni='{}' , correo='{}' , departamento='{}' , categoria='{}' , pass='{}' WHERE nombre='{}';".format(
            dni,correo,departamento,categoria,password,name)
    
        print(query)
        c.execute(query)
        conn.commit()
        c.close()

    except sqlite3.Error as error:
        print("Error mientras se extraían los datos",error)

    finally:
        if (conn):
            conn.close()
            print("Conexion Cerrada")

    return template('modify', cont = 1)

@route('/eliminate')
def eliminate():

    """
    Ruta que solo se activa si eres admin y que sirve para eliminar a un usuario, incluido el propio admin.

    :param conn:
                Objeto sql para realizar las conexiones a la base de datos estipulada
    :param c:
                Cursos de la conexión sql
    :param query:
                Query que se encarga de realizar la operacion adecuada para la consulta sql
    :param result:
                Resultado de la consulta sql
    :param error:
                Cadena con el contenido del error que se ha producido
    :param cont:
                Selector de modos para el template register

    """


    try:


        conn = sqlite3.connect('bottle.db')
        c = conn.cursor()
        
        query = "SELECT nombre FROM usuarios WHERE 1=1;"

        print('\n'+query+'\n')
        
        c.execute(query)
        result = c.fetchall()
        c.close()

    except sqlite3.Error as error:
        print("Error mientras se extraían los datos",error)

    finally:
        if (conn):
            conn.close()
            print("Conexion Cerrada")

    return template('eliminate', cont = 0 , consulta = result)


@route('/eliminate_done', method='POST')
def eliminate_done():

    """
    Ruta que aparece tras realizar la eliminación de algun usuario por parte del administrador, 
    se encarga de manejar toda la información relativa al formulario mandado a la hora de
    eliminar a cualquier usuario.

    :param name:
                Nombre del usuario que queremos borrar.
    :param conn:
                Objeto sql para realizar las conexiones a la base de datos estipulada
    :param c:
                Cursos de la conexión sql
    :param query:
                Query que se encarga de realizar la operacion adecuada para la consulta sql
    :param result:
                Resultado de la consulta sql
    :param error:
                Cadena con el contenido del error que se ha producido
    :param cont:
                Selector de modos para el template register

    """


    try:
        name = request.forms.get('name')

        conn = sqlite3.connect('bottle.db')
        c = conn.cursor()

        query = "DELETE from usuarios where nombre='{}';".format(name)

        print('\n'+query+'\n')

        c.execute(query)
        conn.commit()
        c.close()

    except sqlite3.Error as error:
        print("Error mientras se extraian los datos", error)

    finally:
        if (conn):
            conn.close()
            print("Conexion Cerrada")

    return template('eliminate', cont = 1)
# INICIALIZACIÓN DE EL SERVIDOR


if __name__ == '__main__':

    """
    Llamada al servidor para que empiece la aplicación

        :param host:
                    Parametro para especificar la IP, en este caso usaremos una localhost para trabajar en local
        :param port:
                    Parametro para especificar el puerto, en este caso usaremos el **8080**
        :param reloader:
                    Parámetro muy útil para refrescar el servidor cada vez que realizamos un cambio en el codigo.

    """
    run(host='localhost', port=8080, reloader=True)