# 1. MODELO ENTIDAD RELACIÓN

Recordemos que una entidad es un objeto o concepto del mundo real que se define en una base de datos, para este ejemplo práctico las entidades hacen referencia a  clientes, trayectorias y climas. Note que estas entidades se desprenden de la necesidad de responder las preguntas planteadas posteriormente. A continuación se presentará gráficamente el modelo entidad-relación y se realizará su respectiva interpretación.
 
![](https://github.com/PabloFranco5/FastApi_MapsUdeA/blob/main/diagram.jpeg)

# TABLA USUARIO: 

La tabla USUARIO surge de la necesidad de conocer datos referentes al cliente que está buscando acceder a la información, con esta información se puede realizar análisis posteriores sobre el comportamiento y necesidades generales y específicas que presentan los usuarios.

# TABLA TRAYECTO: 

La tabla TRAYECTO surge de la necesidad de conocer las trayectorias que cada usuario pretende conocer, la ubicación de origen y de destino, el tiempo de trayecto y la distancia recorrida, así como la fecha en la que el usuario realizó la respectiva solicitud de información a la API. 
 
# TABLA CLIMA: 

Esta tabla surge de la necesidad de obtener información sobre las particularidades del clima de la ubicación de destino.


# RELACIONES ENTRE ENTIDADES 
 

# USUARIO - TRAYECTO: 

Estas dos entidades tienen una relación (M/M: muchos a muchos) ya que un usuario puede realizar muchas consultas acerca de diferentes trayectos y un trayecto tiene la posibilidad de ser consultado por muchas personas.
 
# TRAYECTO - CLIMA:

Estas dos entidades tienen una relación (M/M: muchos a muchos) ya que un trayecto puede arrojar diferentes descripciones para el clima de la ubicación de destino dependiendo del momento en que este sea consultado y una descripción del clima tiene la posibilidad de coincidir para diferentes trayectos.
 
# USUARIO - CLIMA:

Estas dos entidades tienen una relación (M/M: muchos a muchos) ya que un usuario puede realizar consultas acerca del clima de diferentes ubicaciones de destino y una descripción del clima tiene la posibilidad de coincidir en las solicitudes de diferentes usuarios.


La tabla de dominio es la tabla USUARIO-TRAYECTO (la tabla principal del modelo) y la tabla de dimensión es la tabla CLIMA (se une a la tabla principal a través de FK). (ver imagen adjunta en el documento para comprender la relación).

# 2. DIAGRAMA DE PROCESOS 

Las APIs de Geolocalización son capaces de integrar el sistema de tu empresa con plataformas de mapas como Google Maps o para este caso en específico la 
plataforma de Mapquest.

Muchas empresas ya han reconocido el potencial de estas herramientas y las utilizan ampliamente en sus estrategias comerciales. Aplicando los servicios 
proporcionados por las APIs de geolocalización ya que estas brindan un gran número de soluciones como acelerar el proceso de compra de tus clientes, 
incrementar la eficiencia del proceso de entrega, ayudar a los compradores a encontrar la mejor tienda y automatizar la planificación y secuenciación de rutas 
de entregas. Además, pueden localizar dispositivos con sus usuarios, permitiendo una serie de servicios y ventajas que veremos a continuación.


## Facilita el acceso a tu empresa
Las APIs de geolocalización ayudan a los compradores a encontrar la mejor tienda para visitar, teniendo en cuenta parámetros como mayor cercanía, 
menor tiempo de espera, productos disponibles, facilidad de llegada y horarios de atención.

Esta herramienta no sólo brinda a los clientes los detalles de la tienda, sino que también detalla el viaje que deben hacer para llegar a ese destino. Como 
funciones complementarias, mantiene a los visitantes en tu sitio para desarrollar aún más tu marca y ofrece una experiencia de usuario eficiente.


## Ayuda a conocer a tu audiencia, haciendo tu marketing más eficiente
La API de Geolocalización es la base del Geomarketing, una estrategia de marketing que se desarrolla a partir de datos de geolocalización, 
implementando acciones en función de los lugares donde las personas viven, circulan o frecuentan.

Este tipo de estrategia permite a una empresa conocer mejor a su público objetivo, entendiendo mejor sus necesidades, preferencias y patrones de consumo. Por 
lo tanto, su marketing se vuelve más eficiente, ya que logra segmentar mejor al público y llegar a él en los momentos más oportunos.

Un buen ejemplo de esto es la tecnología de anuncios de geofencing, uno de los tipos de geomarketing que te permite orientar publicidad relevante a los
consumidores de acuerdo con su historial de ubicaciones.

## Acelera el proceso de compra de tus clientes
Los clientes que compran por internet quieren terminar el proceso de compra lo más rápido posible, generalmente en menos de 10 minutos. Sumar 
demasiados pasos para concretar una compra puede ser perjudicial para tu empresa, de hecho, el 70% de los clientes abandona un proceso de compra en 
línea y el 21% de ellos lo hace por encontrarse con un proceso de pago demasiado largo o complicado.

Para minimizar este margen de rebote, la API de geolocalización permite simplificar el proceso de pago y envío, mejorando de esa manera 
la experiencia del usuario. Además, disminuye la tasa de abandono reduciendo el tiempo necesario para completar el pago, lo que entrega satisfacción a los usuarios.

## Incrementa la productividad
Un ejemplo claro de uso de la API de geolocalización es la actividad de enrutamiento que se vuelve más eficiente al agrupar 
paradas por proximidad estableciendo las mejores rutas. Esto permite realizar un mayor número de entregas en un menor tiempo. Una de 
las grandes ventajas para este proceso es el cálculo en tiempo real y poder aplicar reglas comerciales.

## Reduce los costos
Tanto en la logística, como en los otros procesos que se pueden optimizar, la API de geolocalización sirve para reducir el 
tiempo de ejecución y aumentar la rentabilidad de las operaciones.

![](https://github.com/PabloFranco5/FastApi_MapsUdeA/blob/main/process.jpeg)
 

## PLANTEAMIENTO DEL PROBLEMA

El Sistema de Posicionamiento Global (GPS) proporciona servicios fiables de posicionamiento, navegación y cronometría gratuita e ininterrumpidamente a usuarios en todo el mundo. El sistema proporcionará localización y hora exacta en cualquier condición atmosférica, en cualquier lugar del mundo y sin límite al número de usuarios simultáneos. 

Hoy en día están al alcance de todos en el mercado los pequeños receptores del GPS portátiles. Con esos receptores, el usuario puede determinar con exactitud su ubicación y desplazarse fácilmente al lugar a donde desea trasladarse, ya sea caminando, conduciendo, volando o navegando. El GPS es indispensable en todos los sistemas de transporte del mundo ya que sirve de apoyo a la navegación aérea, terrestre y marítima. Los servicios de emergencia y socorro en casos de desastre dependen del GPS para la localización y coordinación horaria de misiones para salvar vidas. Actividades cotidianas como operaciones bancarias, de telefonía móvil e incluso de las redes de distribución eléctrica, ganan en eficiencia gracias a la exactitud cronométrica que proporciona el GPS. Agricultores, topógrafos, geólogos e innumerables usuarios trabajan de forma más eficiente, segura, económica y precisa gracias a las señales accesibles y gratuitas del GPS.

El desarrollo de la API de GPS pretende, en primera instancia, proporcionar datos de geolocalización, previamente solicitados al proveedor de GPS (Mapquest), que faciliten la identificación de características de interés acerca de rutas definidas por el usuario a partir de una ubicación de origen y una ubicación de destino, y al proveedor para datos del clima (WTTR) para la obtención de particularidades del clima de la ubicación de interés . Mediante la indicación de un punto de origen y un punto de destino, la API extrae una serie de atributos en formato .json que permiten identificar la ruta de acceso a las características de interés. La API de GPS facilitará al usuario información sobre la duración del viaje, la distancia en kilómetros desde el punto de origen al punto de destino, la velocidad promedio, la cantidad aproximada de litros de gasolina necesarios para realizar el recorrido, y las indicaciones durante el recorrido, además de la temperatura y la descripción del clima del lugar de destino.

### Proceso de construcción de la API:

A continuación se dará una breve descripción del proceso llevado a cabo para el desarrollo de la API. 
Nota: Para profundizar en este el proceso de construcción con todos sus detalles, archivos y demás, diríjase al código que se encuentra alojado en el repositorio. 


Selección de las librerías: La librería urllib permite acceder a cualquier recurso alojado en Internet indicado mediante una dirección web. Por su parte, la librería requests facilita el trabajo con peticiones HTTP; particularmente permitirá hacer uso del método GET para extraer información de la URL dada.

```
import requests 
import urllib
```

Del proveedor de información seleccionado, en este caso, Mapquest (brinda  información GPS sobre rutas específicas, similar a Google Maps), se extrae la dirección URL del recurso y la llave que permite autenticar nuestra aplicación con la API de Mapquest.

```
api_url = "http://www.mapquestapi.com/directions/v2/route?"
key = "VUMTeSQl2G6JzINKnAuas25bl9dfkzAk"
```

Se define un punto de origen y un punto de destino de la ruta que posteriormente se va a indicar por el usuario para construir la dirección URL con la que se van a obtener todos los datos provenientes de API Mapquest para esos puntos de origen y destino.

```
origen = imput("Ingresa el punto de partida de tu viaje: ")
destino = imput("¿Hacia dónde te diriges?: ")
url = api_url + urllib.parse.urlencode({"key":key, "from":origen, "to":destino})
```

Se hace uso del método GET de la librería requests para extraer toda información de Mapquest referente a los datos especificados y se reescriben en formato JSON.

```
json_data = requests.get(url).json()
```

Del archivo JSON se obtiene la ruta para determinar el valor de statuscode que indica el éxito de la ejecución de la petición.

```
statuscode = json_data["info"]["satuscode"]
```

Se crea una función que ejecute las acciones requeridas. Dentro de dicha estructura se definen las rutas o direcciones de las características de interés a extraer, como la duración del viaje, la distancia entre las dos ubicaciones seleccionadas y las indicaciones del trayecto para ser visualizadas por el usuario. 

```
def gps(origen, destino):
    url = api_url + urllib.parse.urlencode({"key":key, "from": origen, "to":destino}) 
    json_data = requests.get(url).json()
    duracion_del_viaje = json_data["route"]["formattedTime"]
    distancia = json_data["route"]["distance"] * 1.61
    nombre = ["Duración del viaje", "Distacia a Recorrer"]
    print("Indicaciones del trayecto")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print(each["narrative"])

    return dict(zip(nombre, [duracion_del_viaje, distancia]))
```

Se realiza un proceso análogo para solicitar información del proveedor del clima, WTTR. Se extrae la dirección URL del recurso y la llave que permite autenticar nuestra aplicación con la API de WTTR. Se define el punto de destino como la ubicación de interés. Se crea una función que ejecute las acciones requeridas. Dentro de dicha estructura se definen las rutas o direcciones de las características de interés a extraer, como la duración del viaje, la distancia entre las dos ubicaciones seleccionadas y las indicaciones del trayecto para ser visualizadas por el usuario. 

```
def clima(destino):
    """
    Api que indica el clima de un lugar en específico.
    En este caso deseamos saber el clima que tiene el luegar de destino al que queremos llegar.
    """
    urlclima_o = f"https://es.wttr.in/{destino}?format=j1"
    #urlclima_d = f"https://es.wttr.in/{destino}?format=j1"

    responseclima_o = requests.get(urlclima_o)
    #responseclima_d = requests.get(urlclima_d)
    clima_o = responseclima_o.json()
    #clima_d = responseclima_d.json()

    temperatura_destino = clima_o["current_condition"][0]["temp_C"]
    descripcion = clima_o["current_condition"][0]["lang_es"][0]["value"]
    return temperatura_destino, descripcion

def main(): 
    temperatura_destino, descripcion = clima(destino)
    #print(f"La temperatura actual de {destino} es de {temperatura_destino} °C. {descripcion}")
    return f"La temperatura actual de {destino} es de {temperatura_destino} °C. {descripcion}"

```

Se realiza la creación de la clase Usuario, en ella se declaran los campos necesarios para la identificación del usuario y su información de viaje, estos serán: email, username, puntos de origen y destino. No es necesaria la definición del ID puesto que peewee se encarga de crearlo automáticamente como clave primaria. Posteriormente se añade la clase Meta dentro de la clase Usuario pues esta última será encargada de realizar la conexión a la base de datos.

```
class usuario(peewee.Model):
#    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    punto_salida = peewee.CharField(unique=False, index=True)
    punto_llegada = peewee.CharField(unique=False, index=True)

    class Meta:
        database = db
```

La clase Resumen_viaje contiene los campos necesarios para la identificación del viaje y la información relevante que se desea obtener de este, estos serán: fecha de servicio, puntos de origen y destino, tiempo de trayecto, distancia recorrida y clima; además, contendrá una clave foránea (user) extraída de la entidad usuario, que indicará a qué usuario corresponde dicha información. Posteriormente se añade la clase Meta dentro de la clase Resumen_viaje pues esta última será encargada de realizar la conexión a la base de datos.

```
class resumen_viaje(peewee.Model):
    Fecha_servicio = peewee.DateTimeField(default=datetime.now)
    Lugar_Salida = peewee.CharField(default=False)
    Lugar_Destino = peewee.CharField(default=False)
    Tiempo_trayecto = peewee.CharField(default=False)
    Distancia_recorrida = peewee.CharField(default=False)
    Clima = peewee.CharField(default=False)
    user = peewee.ForeignKeyField(usuario, backref="todos")

    class Meta:
        database = db
```

Se genera una instancia de la clase APIRouter con el parámetro prefix que será igual /api/v1. Esto significa que todas las rutas que se creen con dicha instancia tendrán como prefijo esa url. Tags será una lista con un valor llamado users y será de utilidad para agrupar los endpoints. Se indicará que la petición sea de tipo post usando el método post de router y recibirá varios parámetros. Como primer parámetro se tendrá la ruta /api/v1/user/, el segundo parámetro será status_code que es el estado HTTP que queremos devolver en nuestro endpoint, como lo que vamos a hacer es crear un dato, lo modificaremos y usaremos el estado 201. El parámetro response_model indicará que la respuesta que retornaremos será un modelo de Pydantic de tipo User. Se realiza la conexión a la base de datos ya que será necesaria para la creación del usuario. El parámetro summary será informativo para la documentación.

```
router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/",
    tags = ["users"],
    response_model = UserBase,
    status_code=status.HTTP_201_CREATED,
    dependencies = [Depends(get_db)],
    summary = "Nueva Busqueda"
```

Para la creación del usuario se definirá una función que recibirá una variable llamada user y que será de tipo UserRegister, de modo que la app pueda recibir los datos de interés correspondientes a un usuario en particular, estos serán: username, puntos de origen y destino y retornará esos mismos datos a modo de verificación de recepción de la información.

```
def create_user(user: UserBase = Body(...)):
    User = usuario(
        username = user.username,  
        punto_salida = user.punto_de_salida,
        punto_llegada = user.punto_de_llegada
        )
    User.save()
    return user
```

Se creará un clase UserBase que delimitará las restricciones para los datos username, y puntos de origen y destino, de modo que la aplicación únicamente reciba datos de tipo str en esos campos. En caso de no cumplirse la validación de las restricciones la validación de Pydantic arrojará un error.

```
class UserBase(BaseModel):
    username: str 
    punto_de_salida: str 
    punto_de_llegada: str 
```

Se importan las clases Usuario y Resumen_viaje además del objeto de la base de datos y posteriormente se define una función que se conectará a la base de datos, recibirá una lista de los modelos que queremos convertir en tablas y después cerrará la conexión.

```
from app.v1.model.user_model import usuario
from app.v1.model.viaje_model import resumen_viaje
from app.v1.utils.db import db

def create_tables():
    """
    Creación de las tablas donde se almacena la información relevante
    en donde se resume el viaje y el clima
    """
    with db:
        db.create_tables([usuario, resumen_viaje])
```

Se realiza la creación de la función create_user; esta función recibe como parámetro un modelo de Pydantic de tipo UserBase. Se encargará particularmente de guardar el usuario en la base de datos. Se comprobará si el usuario ingresado ya existe en la base de datos por email o username, en ese caso, se realizará una excepción HTTPException con el código de estado 400 y en el detalle explicaremos la justificación de dicho error. Finalmente se retorna la información del usuario recién creado empleando el modelo User de Pydantic.

```
def create_User(user: UserBase):
    db_user = usuario(
        username = user.username,  
        punto_salida = user.punto_de_salida,
        punto_llegada = user.punto_de_llegada
        )
    db_user.save()
    return UserBase(
        username = db_user.username,
        punto_salida = db_user.punto_salida,
        punto_llegada = db_user.punto_llegada
    )
```

Se realiza la creación de la clase Settings para declarar las variables que guardarán información sobre la conexión y autenticación a la base de datos. Los valores correspondientes a dichas variables se asignan a través de la función GETENV de la librería OS, la cual recibe el nombre asignado a las variables de entorno en el archivo .env; en caso de ser verificada su existencia retornarán su valor, en caso contrario, retornará “None”.

```
class Settings(BaseSettings):

    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')
```

Se instancia la clase Settings para guardar las variables de entorno de la conexión 

```
from app.v1.utils.settings import Settings

settings = Settings()

DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())

```

Posteriormente, se sobreescribe la clase PeeweeConnectionState. 

```
class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]
```

Y se efectúa la conexión a la base de datos de PostgreSQL empleando los parámetros de autenticación y conexión. Las funciones reset_db_state y get_db serán necesarias para la realización de la conexión a la base de datos en todo el proyecto.

```
db = peewee.PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

db._state = PeeweeConnectionState()

async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()
```




