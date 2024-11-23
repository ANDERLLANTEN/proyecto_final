from flask import Flask

app = Flask(__name__)

from app import routes  # Importa tus rutas

#Este es el constructor de la clase 
# que inicializa los atributos mencionados anteriormente. Cada vez que creas una instancia 
# de la clase Ganado, se requiere que pases estos cinco valores como parámetros.