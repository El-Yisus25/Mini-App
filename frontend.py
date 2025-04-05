from backend import Backend
from database import BaseDeDatos

def frontend():
    print("=== Mini App de Tareas ===")
    tarea = input("Escriba el nombre de la tarea y presione Enter: ")  # Simula formulario
    
    respuesta = backend.recibir_tarea(tarea)
    print(respuesta)
    
    tareas_actuales = backend.obtener_tareas()
    print("\nLista actual de tareas:")
    for idx, t in enumerate(tareas_actuales, 1):
        print(f"{idx}. {t}")

# Escalabilidad: puede transformarse en una app web con HTML/JS.
# Mantenibilidad: separado del backend, se puede rediseñar sin afectar la lógica.
# Seguridad: en una app web, se pueden añadir captchas o autenticación.

if __name__ == "__main__":
    db = BaseDeDatos()
    backend = Backend(db)
    frontend()
