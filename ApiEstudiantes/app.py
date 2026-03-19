from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# ------------------------------------------------------------------
# Configuración de la base de datos
# ------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, "estudiantes.db")


def get_db_connection():
    """Abre una conexión a SQLite y devuelve filas como diccionarios."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # permite acceder a columnas por nombre
    return conn


def init_db():
    """Crea la tabla 'estudiantes' si no existe."""
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre   TEXT    NOT NULL,
            carrera  TEXT    NOT NULL,
            semestre INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# ------------------------------------------------------------------
# Endpoints
# ------------------------------------------------------------------

@app.route("/estudiantes", methods=["POST"])
def agregar_estudiante():
    """
    Registra un nuevo estudiante.

    Body JSON esperado:
        {
            "nombre":   "Ana García",
            "carrera":  "Ingeniería en Sistemas",
            "semestre": 4
        }
    """
    datos = request.get_json()

    # --- Validación básica ---
    if not datos:
        return jsonify({"error": "Se requiere un body JSON"}), 400

    campos_requeridos = ["nombre", "carrera", "semestre"]
    for campo in campos_requeridos:
        if campo not in datos:
            return jsonify({"error": f"El campo '{campo}' es requerido"}), 400

    nombre   = datos["nombre"].strip()
    carrera  = datos["carrera"].strip()
    semestre = datos["semestre"]

    if not nombre or not carrera:
        return jsonify({"error": "nombre y carrera no pueden estar vacíos"}), 400

    if not isinstance(semestre, int) or semestre < 1:
        return jsonify({"error": "semestre debe ser un entero positivo"}), 400

    # --- Inserción en la base de datos ---
    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO estudiantes (nombre, carrera, semestre) VALUES (?, ?, ?)",
        (nombre, carrera, semestre)
    )
    conn.commit()
    nuevo_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "mensaje":    "Estudiante registrado correctamente",
        "estudiante": {
            "id":       nuevo_id,
            "nombre":   nombre,
            "carrera":  carrera,
            "semestre": semestre
        }
    }), 201   # 201 Created


@app.route("/estudiantes", methods=["GET"])
def obtener_estudiantes():
    """
    Devuelve todos los estudiantes almacenados.

    Soporta filtro opcional por carrera:
        GET /estudiantes?carrera=Sistemas
    """
    carrera_filtro = request.args.get("carrera")

    conn = get_db_connection()

    if carrera_filtro:
        filas = conn.execute(
            "SELECT * FROM estudiantes WHERE carrera LIKE ?",
            (f"%{carrera_filtro}%",)
        ).fetchall()
    else:
        filas = conn.execute("SELECT * FROM estudiantes").fetchall()

    conn.close()

    # Convertimos cada fila (sqlite3.Row) a diccionario
    estudiantes = [dict(fila) for fila in filas]

    return jsonify({
        "total":       len(estudiantes),
        "estudiantes": estudiantes
    }), 200


# ------------------------------------------------------------------
# Arranque
# ------------------------------------------------------------------
if __name__ == "__main__":
    init_db()                          # Inicializa la BD al arrancar
    print("Base de datos lista en:", DB_PATH)
    app.run(debug=True, port=5000)     # debug=True reinicia al guardar cambios
