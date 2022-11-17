# Explicacion user_schema.py

Ahora vamos a explicar la clase UserBase en profundidad:

Primero definimos la variable que será de tipo EmailStr y será igual a Field. Como primer parámetro enviamos "..." que significa que ese campo será obligatorio, como segundo parámetro recibe example que es un dato informativo para el usuario y que podremos ver en la documentación más adelante.

La segunda variable es username. Esta será de tipo string y aquí recibe dos parámetros nuevos que son min_length y max_length. Esto significa que el string necesitará tener al menos 3 caracteres y como máximo 50 (o los que definamos nosotros) para ser válido. Si no es así la validación de Pydantic lanzará un error.