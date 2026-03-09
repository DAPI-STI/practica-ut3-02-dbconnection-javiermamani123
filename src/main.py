from db import get_connection
from incidencias import crear_incidencia, listar_incidencias_activas

def main():
    try:
        # 1️⃣ Obtener conexión a la base de datos
        conn = get_connection()

        # 2️⃣ Crear una nueva incidencia
        filas = crear_incidencia(
            conn,
            equipo_id=1,  # asegúrate que este equipo existe en la tabla equipos
            descripcion="Prueba de incidencia desde Python",
            prioridad="alta"  # puede ser 'baja', 'media' o 'alta'
        )
        print(f"Filas insertadas: {filas}")

        # 3️⃣ Listar todas las incidencias activas para comprobar
        incidencias = listar_incidencias_activas(conn)
        print("\nIncidencias activas:")
        for i in incidencias:
            print(f"ID: {i['id']}, Equipo: {i['equipo_id']}, Desc: {i['descripcion']}, Prioridad: {i['prioridad']}, Estado: {i['estado']}")

        # 4️⃣ Cerrar conexión
        conn.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

