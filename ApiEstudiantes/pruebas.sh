# ============================================================
# GUÍA DE PRUEBAS — API de Estudiantes con Flask + SQLite
# ============================================================
# Ejecuta cada bloque en tu terminal después de iniciar la API:
#     python app.py

# ------------------------------------------------------------
# 1. REGISTRAR un estudiante (POST /estudiantes)
# ------------------------------------------------------------

# Caso exitoso
curl -X POST http://localhost:5000/estudiantes \
     -H "Content-Type: application/json" \
     -d '{
           "nombre":   "Ana García",
           "carrera":  "Ingeniería en Sistemas",
           "semestre": 4
         }'

# Respuesta esperada (HTTP 201):
# {
#   "mensaje": "Estudiante registrado correctamente",
#   "estudiante": { "id": 1, "nombre": "Ana García", ... }
# }

# ------------------------------------------------------------------

# Error: campo faltante
curl -X POST http://localhost:5000/estudiantes \
     -H "Content-Type: application/json" \
     -d '{"nombre": "Sin carrera"}'

# Respuesta esperada (HTTP 400):
# { "error": "El campo 'carrera' es requerido" }

# ------------------------------------------------------------
# 2. CONSULTAR todos los estudiantes (GET /estudiantes)
# ------------------------------------------------------------

curl http://localhost:5000/estudiantes

# Respuesta esperada (HTTP 200):
# {
#   "total": 1,
#   "estudiantes": [
#     { "id": 1, "nombre": "Ana García", "carrera": "...", "semestre": 4 }
#   ]
# }

# ------------------------------------------------------------
# 3. FILTRAR por carrera (query param opcional)
# ------------------------------------------------------------

curl "http://localhost:5000/estudiantes?carrera=Sistemas"

# Devuelve solo los estudiantes cuya carrera contenga "Sistemas"


# ============================================================
# FLUJO COMPLETO PARA PROBAR EN POSTMAN
# ============================================================
# Método : POST
# URL    : http://localhost:5000/estudiantes
# Headers: Content-Type: application/json
# Body (raw JSON):
# {
#   "nombre":   "Luis Ramírez",
#   "carrera":  "Contaduría Pública",
#   "semestre": 6
# }
#
# Método : GET
# URL    : http://localhost:5000/estudiantes
# (sin body, sin headers extra)
