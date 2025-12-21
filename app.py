from flask import Flask, render_template, request, redirect, url_for
from src.database import DBManager
from src.modelos import Tarea, Proyecto

# Inicialización de la aplicación Flask
app = Flask(__name__)
db_manager = DBManager()

# Ruta principal que muestra las tareas y proyectos     
@app.route('/')
def index():
    tareas_pendientes = db_manager.obtener_tareas(estado='Pendiente')
    proyectos = db_manager.obtener_proyectos()
    
    # Renderizado de la plantilla con las tareas y proyectos
    return render_template(index.html,
                           tareas=tareas_pendientes,
                           proyectos=proyectos)

# Ruta para agregar una nueva tarea

