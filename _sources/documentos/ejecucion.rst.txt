Ejecución
==========

.. toctree::
   :maxdepth: 2

Cuando abrimos el programa ante nosotros se nos muestra 3 posibles acciones:

1. Puedes realizar una búsqueda de usuario.
2. Puedes registrarte.
3. Puedes iniciar sesión.

A continuación, se muestra una descripción detallada paso a paso de cada una de ellas

Realizar una búsqueda
+++++++++++++++++++++

Si lo que se quiere es realizar una búsqueda, nos vamos al menú que 
se muestra llamado *Búsqueda de Usuario*. En este nos dan las opciones de datos con los que podemos realizar una búsqueda:

* **Nombre:** Podemos realizar una búsqueda introduciendo el nombre de la persona que estamos buscando, ya sea el nombre, el apellido, o ambas cosas.
* **Departamentos:** Se muestra una lista de los departamentos existentes y solo tenemos que seleccionar uno.
* **Categorias:** Se muestra una lista de las categorías existentes y solo tenemos que seleccionar una.
* **Asignaturas:** Se muestra una lista de las asignaturas existentes y solo tenemos que seleccionar una.
* **DNI:** Podemos introducir el DNI completo de la persona que estamos buscando.

Podemos rellenar todas las opciones de búsqueda, solo algunas, o incluso ninguna. Una vez introducido los datos deseados, 
presionamos el botón *Buscar* y se nos abrirá un apartado a la derecha de la pantalla con los resultados.

Registrarse
+++++++++++
Si, por lo contrario, se quiere registrar. Pulsamos sobre la opción Regístrate y nos mostrará un menú preparado para ello. 
El menú está compuesto por los siguientes apartados:

* **Nombre y Apellidos:** Se introduce el nombre y apellidos de la persona que se está registrando.

* **Contraseña:** Nos pide una contraseña con la que posteriormente podremos identificarnos. Esta contraseña tiene que ser de un máximo de 20 caracteres.

* **DNI:** Se introduce el DNI de la persona que se está registrando.

* **Correo Electrónico:** Se requiere un correo electrónico perteneciente a la persona. Este posteriormente será nuestra forma de identificarnos cuando intentemos iniciar sesión.

* **Seleccionar Departamento:** Se muestra una lista de los departamentos a los que puede pertenecer el usuario.

* **Seleccionar Categoría:** Se muestra una lista de las categorías a los que puede pertenecer el usuario.
  
   - Si en este apartado seleccionamos la categoría PDI, cuando pulsemos Registro se nos mostrará una lista de asignaturas a las que puede pertenecer el usuario. Puede seleccionar varias asignaturas.

Una vez hemos acabado de rellenar los datos, pulsamos Registro, se nos mostrará un mensaje de registro exitoso si los datos introducidos están bien, 
y una vez acabado, pulsamos Inicio.

Identificarse
+++++++++++++
Si, finalmente, se quiere identificar. Pulsamos sobre la opción Identifícate y nos mostrará un menú preparado para ello. El menú está compuesto por los siguientes apartados:

* **Correo Electrónico:** Se requiere el correo electrónico que fue introducido cuando el usuario realizó el registro.
* **Contraseña:** Se requiere la contraseña que fue introducida en el proceso de registro.

Al interactuar con este menú, puede pasar lo siguiente:

* Si metes un correo electrónico que no existe en la base de datos. Al intentar iniciar sesión te muestra un mensaje de error al introducir los datos, y vuelve a mostrarte el menú de inicio de sesión.
* Si metes una contraseña incorrecta, muestra mensaje de error y vuelve a mostrar el menú de inicio de sesión.

Todo lo anteriormente explicado es desde el punto de vista de un usuario normal, pero existe un usuario denominado como administrador, 
que al iniciar sesión tiene funciones especiales. El administrador además de realizar las búsquedas, puede realizar:

* **Modificar Usuario:** Con esta función el administrador puede modificar cualquier usuario (incluyendo a si mismo). Cuando accedes a esta opción se muestra lo siguiente:
  
   - *Una lista con los usuarios existentes*, para seleccionar al usuario que se desea modificar.
   - *Contraseña*: Puede cambiar la contraseña de acceso del usuario.
   - *DNI*: Puede introducir un número nuevo.
   - *Correo Electrónico*: Puede cambiar el correo del usuario (hay que tener en cuenta que, si se modifica, el usuario debe usar el nuevo correo para acceder).
   - *Seleccionar Departamento*: Puede cambiar de departamento al usuario seleccionando uno de los que se muestra en la lista.
   - *Seleccionar Categoría*: Se muestra una lista con las categorías, y el administrador podrá seleccionar la que quiera asignarle al usuario.
   
Cuando todo este rellenado, se selecciona la opción Modificar y se modificaran los datos del usuario de forma exitosa.

* **Eliminar Usuario:** Con esta función el administrador puede eliminar cualquier usuario. Cuando selecciona esta opción, se le muestra la lista de usuarios, una vez seleccionado uno, se pulsa Eliminar, y se eliminará el usuario de forma exitosa.
