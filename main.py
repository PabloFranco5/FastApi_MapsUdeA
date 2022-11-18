from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Hello World"}


PENDIENTE REVISAR LAS COLUMNAS DE LAS TABLAS PARA CONTINUAR 
