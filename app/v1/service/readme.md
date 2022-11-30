# Explicacion user_service.py

En este archivo se realiza la creación de la función create_user; esta función recibe como parámetro un modelo de Pydantic de tipo UserBase. Se encargará particularmente de guardar el usuario en la base de datos. Se comprobará si el usuario ingresado ya existe en la base de datos por email o username, en ese caso, se realizará una excepción HTTPException con el código de estado 400 y en el detalle explicaremos la justificación de dicho error. Finalmente se retorna la información del usuario recién creado empleando el modelo User de Pydantic.

