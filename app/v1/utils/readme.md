
# Explicación settings.py

Se realiza la creación de la clase Settings para declarar las variables que guardarán información sobre la conexión y autenticación a la base de datos. Los valores correspondientes a dichas variables se asignan a través de la función GETENV de la librería OS, la cual recibe el nombre asignado a las variables de entorno en el archivo .env; en caso de ser verificada su existencia retornarán su valor, en caso contrario, retornará “None”.


# Explciación db.py (la conexion a la base de datos)

Se instancia la clase Settings para guardar las variables de entorno de la conexión. Posteriormente, se sobreescribe la clase PeeweeConnectionState. Finalmente se efectúa la conexión a la base de datos de PostgreSQL empleando los parámetros de autenticación y conexión. Las funciones reset_db_state y get_db serán necesarias para la realización de la conexión a la base de datos en todo el proyecto.


