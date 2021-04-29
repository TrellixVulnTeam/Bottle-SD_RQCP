Instalación de Herramientas 
===========================

.. toctree::
   :maxdepth: 4


GitHub
^^^^^^
Esta aplicación de búsqueda, modificación, registro y eliminación de usuarios se encuentra alojada en GitHub, para
entrar, acceder a través de este enlace: `BottlePy <https://github.com/Mwazoski/Bottle-SD>`_.

Una vez accedemos al repositorio, encontraremos un árbol de directorios
    
    - docs
    - source 


Docs
    Tiene todo lo relacionado con la documentación del software, tanto la generación automatica de la documentación interna
    a través de la herramienta `Sphynx <https://www.sphinx-doc.org/en/master/>`_, que permite auto-generar código de Python siguiendo simplemente unos patrones de comentado
    de código, como la generación del HTML y Latex del resto de tipos de documentación.

    Dejando la documentación expuesta al público, se facilita para el próximo desarrollador de un proyecto abierto como este, la posibilidad
    de seguir contribuyendo, no solo con la parte del código, si también documentando todas las nuevas características que se va añadiendo a 
    esta APIRest.

    Todo esto tiene una intención meramente expositiva, puesto que este proyecto dudo que se siga desarrollando.

Source
    En el directorio source encontramos:
        
        - Los templates HTML
        - Base de Datos Sqlite3
        - Archivo de configuración **"requirements.txt"**
        - Scripts **Run.py** y **Runsql.py**
   
Instalación
^^^^^^^^^^^^^

Lo primero que realizaremos para manejar esta app será un `git clone`

.. code-block:: BASH

    $ git clone https://github.com/Mwazoski/Bottle-SD.git

Una vez hallamos descargado el proyecto, entraremos dentro del directorio source, donde crearemos nuestro
entorno virtual para poder, más tarde, realizar la instalación de todos los módulos necesarios para manejar 
tanto la documentación, como el código.

Creación de un entorno Virtual `Venv`_

==============

Cuando hayamos creado el espacio virtual y estemos dentro de él, tendremos que instalar mediante la herramienta **pip**, todas las 
dependencias que esta APIRest requiere. Simplemento ejecutamos el comando

.. code-block:: BASH

    $ pip install -r requirements.txt

Este cogerá del archivo *requirements.txt* todas las dependencias que se requieren, includas la especificación de sus versiones.

Una vez hemos instalado todas las dependencias, estaremos listos para volver a la carpeta **/source** y poder lanzar el programa,
esto lo realizaremos mediante la invocación del intérprete python.

.. code-block:: BASH

    $ python run.py


Venv
++++
**Introducción**

Un entorno virtual de Python es un ambiente creado con el objetivo de aislar recursos como librerías y entorno de ejecución, 
del sistema principal o de otros entornos virtuales. Lo anterior significa que en el mismo sistema, maquina o computadora, 
es posible tener instaladas multiples versiones de una misma librería sin crear ningún tipo de conflicto.

Para poder utilizar este simple pero poderoso concepto es necesario instalar una utilidad que permita gestionar la creación
y utilización de dichos entornos virtuales llamada venv.

El módulo venv proporciona soporte para crear «entornos virtuales» ligeros con sus propios directorios de ubicación, 
aislados opcionalmente de los directorios de ubicación del sistema. Cada entorno virtual tiene su propio binario Python 
(que coincide con la versión del binario que se utilizó para crear este entorno) y puede tener su propio conjunto independiente 
de paquetes Python instalados en sus directorios de ubicación.

**Como usar Venv**

.. code-block:: BASH

    # python3 venv carpeta_destino
    
    $ python3 venv mientorno

Una vez se ha creado el entorno virtual, debemos entrar en dicho entorno.

.. code-block:: BASH

    $ source mientorno/bin/activate

Una vez ejecutado este comando, estaremos dentro del entorno virtual, sabremos esto ya que nuestra consola
ahora aparecerá de la siguiente manera.

.. code-block:: BASH

    (mientorno) user@user:~/


Add-Ons
^^^^^^^

Esta APIRest desbloquea mucha de sus funciones, gracias al usuario administrador, el cual es capaz de realizar acciones
adicionales, por defecto, el usuario adminisitrador:

Admin
    - **Usuario:** admin
    - **Correo Electrónico:** admin@uca.es
    - **Contraseña:** admin


Logeandonos con estas credenciales podremos obtener acceso a diferentes funcionalidades como
    
    - *Eliminar Usuarios*
    - *Modificar Usuarios*
     
Es decir, casi que tendremos un manejo básico de la Base de Datos, a través de una Interfaz.

Base de Datos
+++++++++++++

Como Base de Datos, hemos empleado sqlite3. `SQLite <https://docs.python.org/es/3.10/library/sqlite3.html>`_ , es una biblioteca de 
C que provee una base de datos ligera basada en disco que no requiere un proceso de servidor separado y permite acceder 
a la base de datos usando una variación no estándar del lenguaje de consulta SQL. Esta se convierte en una Base de Datos 
perfecta para proyectos pequeños como este.

Para realizar una modificación en la Base de Datos, iremos al archivo **runsql.py**. Aqui encontraremos
este código:

.. code-block:: PYTHON

    import sqlite3

    def databasecreate():

        print("Creando la base de datos");

        # TABLA DE USUARIOS

        conn = sqlite3.connect('bottle.db')
        conn.execute("CREATE TABLE usuarios (nombre char(50) PRIMARY KEY NOT NULL, dni char(10) NOT NULL, pass char(20) NOT NULL, correo char(60) NOT NULL, departamento char(100), categoria char(5))")
        conn.execute("INSERT INTO usuarios (nombre, dni, correo, departamento, categoria, pass) VALUES ('admin','admin','admin@uca.es','Administracion','ADM', 'admin') ")
        
        # TABLA DE ASIGNATURAS

        conn.execute("CREATE TABLE asignatura (id INTEGER PRIMARY KEY, nombre char(100))")
        
        while True:

            consulta = input("Introduce una asignatura (n) para cancelar: ")
            
            if consulta == 'n':
                break
            else:
                query = "INSERT INTO asignatura (nombre) VALUES ('{}')".format(consulta)
                conn.execute(query)
            
        # TABLA DE PROF_ASIG

        conn.execute("CREATE TABLE prof_asig (profesor char(50), asignatura char(100), foreign key(profesor) references usuarios(nombre) );")

        conn.commit()
        conn.close()
        print("\n Base de datos creada")    


    if __name__ == '__main__':

        databasecreate()


.. warning:: **No cambiar el esquema de las tablas, solo la información en ellas.**

Para cambiar la información de las tablas, simplemente sustituiremos las columnas de correo y contraseña del admin, dejando 
el nombre **admin** tal y como está. Así pues podremos tener un usuario admin, con nuestro correo y contraseña personalizado.