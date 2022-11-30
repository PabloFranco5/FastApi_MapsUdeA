# Explicación user_model.py

En este archivo se realiza la creación de la clase Usuario, en ella se declaran los campos necesarios para la identificación del usuario y su información de viaje, estos serán: email, username, puntos de origen y destino. No es necesaria la definición del ID puesto que peewee se encarga de crearlo automáticamente como clave primaria. Posteriormente se añade la clase Meta dentro de la clase Usuario pues esta última será encargada de realizar la conexión a la base de datos.




# Explicación viaje_model.py 

En este archivo se realiza la creación de la clase Resumen_viaje, la cual contiene los campos necesarios para la identificación del viaje y la información relevante que se desea obtener de este, estos serán: fecha de servicio, puntos de origen y destino, tiempo de trayecto, distancia recorrida y clima; además, contendrá una clave foránea (user) extraída de la entidad usuario, que indicará a qué usuario corresponde dicha información. Posteriormente se añade la clase Meta dentro de la clase Resumen_viaje pues esta última será encargada de realizar la conexión a la base de datos.
