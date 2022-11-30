# Explicacion user_schema.py

Ahora vamos a explicar la clase UserBase en profundidad:

Se define la variable que será de tipo EmailStr y será igual a Field. Como primer parámetro enviamos "..." que significa que ese campo será obligatorio, como segundo parámetro recibe example que es un dato informativo para el usuario y que podremos ver en la documentación más adelante.

Se realiza la creación de la clase UserBase que delimitará las restricciones para los datos username, y puntos de origen y destino, de modo que la aplicación únicamente reciba datos de tipo str en esos campos. En caso de no cumplirse la validación de las restricciones la validación de Pydantic arrojará lanzará un error.