BottlePy - Sistemas Distribuidos - Practica 3
=============================================

.. image:: bottlelogo.png
      :align: center
      :alt: BottlePy
      :height: 500
      :width: 500 


En esta práctica vamos a trabajar con el framework Bottle visto en el Seminario 3. 
La idea es crear un servicio web de directorio similar al `Directorio de la Universidad de Cádiz <https://directorio.uca.es/cau/directorio.do>`_.

El servicio deberá contar con un listado (evidentemente ficticio) del personal de la UCA, y cada miembro 
contará con los siguientes atributos:

   - DNI.
   - Nombre Completo.
   - Correo Electronico.
   - Departamento.
   - Categoria.
   - Lista de Asignaturas.

El servicio web deberá contar, al menos, con los siguientes **endpoints**:

      - Dar de alta a un nuevo miembro.
      - Modificar los datos de un miembro.
      - Consultar la lista de todos los miembros de la Universidad.
      - Hacer una Búsqueda por DNI.
      - Obtener una lista de miembros según categoria.


**Mejoras**
      - Crear un endpoint para eliminar un miembro mediante una operación HTTP DELETE
      - Utilizar alguna forma de persistencia de datos, almacenando la información de los miembros en unfichero o en una base de datos.
      - Habilitar una búsqueda parcial por nombre.
      - Habilitar una búsqueda paramétrica en la que se pueda elegir por qué criterio buscar.
      - Implementar una búsqueda inversa por asignaturas, listando los miembros PDI que pertenezcan a una asignatura.
      - Verificar que los datos introducidos al añadir un nuevo miembro son correctos, como por ejemplo la letra del DNI.
      - Otros endpoints adicionales que el estudiante considere oportunos.


.. toctree::
   :maxdepth: 2
   :caption: Indice:

   documentos/instalacion
   documentos/autores
   documentos/ejecucion
   documentos/codigo
   
   