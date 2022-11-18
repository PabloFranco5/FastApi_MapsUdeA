# Explicación user_router.py

Una vez hecho esto, generamos una instancia de la clase APIRouter con el parámetro prefix que será igual /api/v1. Esto significará que todas las rutas que creemos con esa instancia tendrán como prefijo esa url.

El segundo parámetro es tags que será una lista con un valor llamado users. A nivel de código no implica nada, pero nos servirá para agrupar nuestros endpoints por tipo cuando más adelante veamos el funcionamiento de la documentación que genera FastAPI automáticamente.

Ahora que ya tenemos la instancia de APIRouter configurada es hora de añadir nuestro primer endpoint. Para ello, al igual que cuando definimos el endpoint para retornar el mensaje "Hello world", creamos un decorador con router.

Indicamos que la petición será de tipo post usando él (valga la redundancia) método post de router y como parámetros recibirá varios parámetros.

El primer parámetro serla la ruta que nosotros la llamaremos "/user/" y que realmente como añadimos un prefijo en la instancia de APIRouter será /api/v1/user/.

El siguiente parámetro sería status_code que es el estado HTTP que queremos devolver en nuestro endpoint. Es un campo opcional y si no lo añadimos por defecto será el estado 200 OK, pero como lo que vamos a hacer es crear un dato, lo modificaremos y usaremos el estado 201.

El parámetro response_model indicará que la respuesta que retornaremos será un modelo de Pydantic de tipo User.

Como dependencies pasamos la conexión a la base de datos, ya que la necesitaremos para crear al usuario.

Y por último, el parámetro summary será informativo para la documentación.

Ahora que terminamos con el decorador, definimos la función. Esta recibirá una variable llamada user y que será de tipo UserRegister e igual a Body. Como cuando creamos los datos del modelo de Pydantic y Field, en el caso de que Body recibirá por parámetro "..." Significará que el campo es obligatorio.