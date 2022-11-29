# Explicacion user_model.py

Esta clase extiende de peewee.Model y en ella declaramos los campos que vamos a necesitar que será un email, username los puntos de partida y llegada del usuario. El id no es necesario definirlo, ya que peewee se encargará de crearlo automáticamente como clave primaria y autoincrement.

Después añadimos la clase Meta dentro de la clase User que contendrá la conexión a la base de datos.

Hola


# Explicacion viaje_model.py 

CAMBIAR EXPLICACION 

En este caso tendremos cuatro columnas (más el id que se genera automáticamente). El campo title será una breve descripción de la tarea a realizar, created_at será la fecha de creación, un booleano llamado is_done para indicar si la tarea ya ha sido realizada o no que por defecto se guardará como false y una clave foránea user para indicar a que usuario corresponde el todo. Esto guardará en la base de datos como un campo llamado user_id.
