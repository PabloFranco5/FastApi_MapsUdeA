# Explicación funciones.py

Selección de las librerías para extracción de información de la web: La librería urllib permite acceder a cualquier recurso alojado en Internet indicado mediante una dirección web. Por su parte, la librería requests facilita el trabajo con peticiones HTTP; particularmente permitirá hacer uso del método GET para extraer información de la URL dada.

Del proveedor de información seleccionado, en este caso, Mapquest (brinda  información GPS sobre rutas específicas, similar a Google Maps), se extrae la dirección URL del recurso y la llave que permite autenticar nuestra aplicación con la API de Mapquest.

Se define un punto de origen y un punto de destino de la ruta que posteriormente se va a indicar por el usuario para construir la dirección URL con la que se van a obtener todos los datos provenientes de API Mapquest para esos puntos de origen y destino.

Se hace uso del método GET de la librería requests para extraer toda información de Mapquest referente a los datos especificados y se reescriben en formato JSON. 

Del archivo JSON se obtiene la ruta para determinar el valor de statuscode que indica el éxito de la ejecución de la petición. 

Se crea una función que ejecute las acciones requeridas. Dentro de dicha estructura se definen las rutas o direcciones de las características de interés a extraer, como la duración del viaje, la distancia entre las dos ubicaciones seleccionadas y las indicaciones del trayecto para ser visualizadas por el usuario. 

Se realiza un proceso análogo para solicitar información del proveedor del clima, WTTR. Se extrae la dirección URL del recurso y la llave que permite autenticar nuestra aplicación con la API de WTTR. Se define el punto de destino como la ubicación de interés. Se crea una función que ejecute las acciones requeridas. Dentro de dicha estructura se definen las rutas o direcciones de las características de interés a extraer, como la temperatura de la ubicación de destino y su respectiva descripción para ser visualizadas por el usuario. 
