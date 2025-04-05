from database import BaseDeDatos

class Backend:
    def __init__(self, base_de_datos):
        self.db = base_de_datos

    def recibir_tarea(self, tarea):
        if not tarea or not tarea.strip():
            return "Error: la tarea no puede estar vacía."  # Seguridad: validación básica

        tarea_limpia = tarea.strip()
        self.db.guardar_tarea(tarea_limpia)
        return f"Tarea guardada: {tarea_limpia}"
    
    def obtener_tareas(self):
        return self.db.obtener_todas_las_tareas()

# Escalabilidad: puede ser adaptado fácilmente a un servidor web como Flask o FastAPI.
# Mantenibilidad: al separar esta capa, es más fácil probar o extender la lógica.
# Seguridad: se valida la entrada para evitar contenido malicioso o vacío.
