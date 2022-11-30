# Modelo Entidad Relación.
 
El modelo entidad relación que se maneja en la base de datos es:

IMG del modelo entidad relación.
Imagen

## Interpretación del modelo entidad-relación, tablas dominio y tablas de dimensiones.

Recordemos que una entidad es un objeto o concepto del mundo real que se define en una base de datos, para este ejemplo práctico las entidades hacen referencia a  clientes, trayectorias y climas. Note que estas entidades se desprenden de la necesidad de responder las preguntas planteadas anteriormente. A continuación, explicaremos la creación de cada tabla utilizada en el modelo:


### Tabla Cliente: 
Nace de la necesidad de conocer datos referentes al cliente que está buscando acceder a la información, con esta información se puede realziar análisis posteriores sobre el comportamiento y necesidades genrales y especificas que presentan los usuarios.


### Tabla Trayectorias: 
Nace de la necesidad de conocer las trayectorias que cada usuario pretende conocer, el lugar de origen o de partida del gps y lugar de llegada de la persona.


### Tabla clima: 
Esta tabla nace de la necesidad de obtener información sobre las particularidades del clima deel ugar de destino.


### RELACIONES: Esta parte hay que cambiarla. con las tablas nuevas de resto todo listo :)
Muchos a Muchos (M/M o N/N)
TABLA PRODUCTO --- TABLA VENTA: 
Dichas entidades se relacionan (M/M) ya que una venta PUEDE contar con varios productos y un producto PUEDE venderse muchas veces
Uno a Muchos (1/M o 1/N)
TABLA CLIENTE --- TABLA PRODUCTO-VENTA: 
Notamos que la relación que existe en estas tablas es de (1/M) ya que un solo cliente PUEDE realizar varias compras, pero una compra o venta solo ESTÁ a nombre de una sola persona o cliente.

TABLA CLIENTE --- TABLA TIENDA: 
La relación de estas tablas es igualmente (1/M) ya que un cliente puede COMPRAR en varias tiendas, pero varias compras en varias tiendas solo pueden APLICARSE a un solo cliente (esto porque la venta está a nombre de una sola persona no de muchas).

TABLA TIENDA --- TABLA PAÍS: 
La relación de estas tablas es (1/M) ya que un país PUEDE tener varias tiendas o sucursales, pero una sucursal no puede estar en varios países al mismo tiempo.

TABLA TIENDA --- TABLA VENTA: 
La relación de estas tablas es de (1/M) ya que una tienda puede REALIZAR varias ventas, pero las ventas realizadas solo pueden hacerse en una sucursal, es decir, al realizarse una venta esta solo se realiza en una sola sucursal o tienda y no en muchas.

Para finalizar, La tabla de dominio es la tabla cliente-trayectoria (la tabla principal del modelo) y las tablas de dimensión serán la tabla clima (se unen a la tabla principal a través de FK). (ver imagen adjunta en el documento para comprender la relación).

 
# Diagramas de procesos.
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

IMAGEN
 

# Planteamiento del problema. 
El desarrollo de la API de GPS pretende, en primera instancia, proporcionar datos de geolocalización, previamente solicitados al proveedor de GPS (Mapquest), 
que faciliten la identificación de características de interés acerca de rutas definidas por el usuario. Mediante la indicación de un punto de origen y un punto 
de destino, la API extrae una serie de atributos en formato .json que permiten identificar la ruta de acceso a las características de interés. La API de GPS 
facilitará al usuario información sobre la duración del viaje, la distancia en kilómetros desde el punto de origen al punto de destino, la velocidad promedio, 
la cantidad aproximada de litros de gasolina necesarios para realizar el recorrido, y las indicaciones durante el recorrido.

### Proceso de construcción de la API:
Selección de las librerías: La librería urllib permite acceder a cualquier recurso alojado en Internet indicado mediante una dirección web. Por su parte, 
la librería requests facilita el trabajo con peticiones HTTP; particularmente permitirá hacer uso del método GET para extraer información de la URL dada.

IMG


Del proveedor de información seleccionado, en este caso, Mapquest (brinda  información GPS sobre rutas específicas, similar a Google Maps), 
se extrae la dirección URL del recurso y la llave que permite autenticar nuestra aplicación con la API de Mapquest.

IMG

Se define un punto de origen y un punto de destino de la ruta que posteriormente se va a indicar por el usuario para construir la dirección URL 
con la que se van a obtener todos los datos provenientes de API Mapquest para esos puntos de origen y destino.

IMG


Se hace uso del método GET de la librería requests para extraer toda información de Mapquest referente a los datos especificados y se reescriben en formato JSON.

IMG

Del archivo JSON se obtiene la ruta para determinar el valor de statuscode que indica el éxito de la ejecución de la petición.

Se crea una función que ejecute las acciones requeridas. Dentro de dicha estructura se definen las rutas o direcciones de las características de 
interés a extraer, como la duración del viaje, la distancia entre las dos ubicaciones seleccionadas y las indicaciones del trayecto para ser visualizadas 
por el usuario. 

IMG

Se realiza un proceso análogo para solicitar información del proveedor del clima, WTTR. Se extrae la dirección URL del recurso y la llave que permite 
autenticar nuestra aplicación con la API de WTTR. Se define el punto de destino como la ubicación de interés. Se crea una función que ejecute las acciones 
requeridas. Dentro de dicha estructura se definen las rutas o direcciones de las características de interés a extraer, como la duración del viaje, la distancia 
entre las dos ubicaciones seleccionadas y las indicaciones del trayecto para ser visualizadas por el usuario. 

IMG


