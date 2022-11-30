# Explicación user_router.py

Se genera una instancia de la clase APIRouter con el parámetro prefix que será igual /api/v1. Esto significará que todas las rutas que creemos con esa instancia tendrán como prefijo esa url.

El parámetro es tags que será una lista con un valor llamado users. A nivel de código no implica nada, pero servirá para agrupar los endpoints por tipo cuando más adelante veamos el funcionamiento de la documentación que genera FastAPI automáticamente.

Para añadir el primer endpoint es necesario crear un decorador con router. La petición será de tipo post usando el método post de router y recibirá varios parámetros.

El primer parámetro será la ruta "/user/", como fue añadido un prefijo en la instancia de APIRouter será entonces "/api/v1/user/". 

El siguiente parámetro sería status_code que es el estado HTTP que se desea devolver en el endpoint. Es un campo opcional (si no se añade, por defecto será el estado 200 OK), como se realizará la creación un dato, usará el estado 201.
El parámetro response_model indicará que la respuesta a retornar será un modelo de Pydantic de tipo User. Se realiza la conexión a la base de datos ya que será necesaria para la creación del usuario. El parámetro summary será informativo para la documentación.

Para la creación del usuario se definirá una función que recibirá una variable llamada user y que será de tipo UserRegister e igual a Body, de modo que la app pueda recibir los datos de interés correspondientes a un usuario en particular, estos serán: username, puntos de origen y destino y retornará esos mismos datos a modo de verificación de recepción de la información. En caso de que Body recibiera por parámetro "..." el campo será obligatorio.
