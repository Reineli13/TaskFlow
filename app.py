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
    return render_template('index.html',
                           tareas=tareas_pendientes,
                           proyectos=proyectos)


# Ruta para agregar una nueva tarea
@app.route('/crear', methods=['GET', 'POST'])
def crear_tarea():

    proyectos = db_manager.obtener_proyectos()

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        limite = request.form.get('fecha_limite')
        prioridad = request.form.get('prioridad')
        
        proyecto_id = int(request.form.get('proyecto_id'))
    
        nueva_tarea = Tarea(
            titulo=titulo,
            descripcion=descripcion,
            fecha_limite=limite,
            prioridad=prioridad,
            proyecto_id=proyecto_id
        )

        db_manager.crear_tarea(nueva_tarea)

        return redirect(url_for('index'))
    
    return render_template('formulario_tarea.html', proyectos=proyectos)

# Ruta para iniciar la aplicación
if __name__ == '__main__':
    
    db_manager.crear_tablas()
    print('Iniciando servidor Flask...')
    app.run(debug=True)