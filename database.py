import json
import os

ARCHIVO_DB = "tareas.json"

class BaseDeDatos:
    def __init__(self):
        self.tareas = self._cargar_desde_archivo()

    def _cargar_desde_archivo(self):
        if os.path.exists(ARCHIVO_DB):
            with open(ARCHIVO_DB, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _guardar_en_archivo(self):
        with open(ARCHIVO_DB, "w", encoding="utf-8") as f:
            json.dump(self.tareas, f, indent=2, ensure_ascii=False)

    def guardar_tarea(self, tarea):
        self.tareas.append(tarea)
        self._guardar_en_archivo()
        return True

    def obtener_todas_las_tareas(self):
        return self.tareas

# Escalabilidad: se puede cambiar esta clase por una base de datos real (MongoDB, PostgreSQL).
# Mantenibilidad: el backend no necesita saber cómo se guardan los datos internamente.
