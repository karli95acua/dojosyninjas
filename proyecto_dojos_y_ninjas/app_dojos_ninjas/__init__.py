from flask import Flask

app = Flask(__name__)
app.secret_key = "esto es secreto"
BASE_DATOS = "esquemas_dojos_y_ninjas"