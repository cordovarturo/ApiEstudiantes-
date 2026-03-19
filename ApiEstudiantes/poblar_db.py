"""
poblar_db.py
------------
Ejecuta este script UNA vez para insertar datos de ejemplo
y verificar que la base de datos funciona correctamente.

Uso:
    python poblar_db.py
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "estudiantes.db")

datos_ejemplo = [
    ("Ana García",     "Ingeniería en Sistemas",  4),
    ("Luis Ramírez",   "Contaduría Pública",       6),
    ("Sofía Mendoza",  "Diseño Gráfico",           2),
    ("Carlos Torres",  "Ingeniería en Sistemas",   8),
    ("Valeria López",  "Administración",           3),
]

def main():
    if not os.path.exists(DB_PATH):
        print("ERROR: La base de datos no existe. Ejecuta primero 'python app.py'.")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.executemany(
        "INSERT INTO estudiantes (nombre, carrera, semestre) VALUES (?, ?, ?)",
        datos_ejemplo
    )
    conn.commit()

    total = conn.execute("SELECT COUNT(*) FROM estudiantes").fetchone()[0]
    conn.close()

    print(f"✓ Se insertaron {len(datos_ejemplo)} registros.")
    print(f"  Total de estudiantes en la BD: {total}")

if __name__ == "__main__":
    main()
