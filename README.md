# API de Estudiantes — Flask + SQLite

Proyecto de práctica para aprender a conectar Flask con una base de datos
y realizar operaciones básicas de almacenamiento y consulta.

## Archivos del proyecto

```
api_estudiantes/
├── app.py          ← API principal (ejecutar este)
├── poblar_db.py    ← Script para insertar datos de ejemplo
├── pruebas.sh      ← Comandos curl para probar la API
└── estudiantes.db  ← Se crea automáticamente al ejecutar app.py
```

## Instalación

```bash
# 1. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 2. Instalar Flask
pip install flask
```

## Ejecutar la API

```bash
python app.py
```

Verás en la terminal:
```
Base de datos lista en: /ruta/estudiantes.db
 * Running on http://127.0.0.1:5000
```

## Endpoints disponibles

| Método | Ruta           | Descripción                        |
|--------|----------------|------------------------------------|
| POST   | /estudiantes   | Registra un nuevo estudiante       |
| GET    | /estudiantes   | Consulta todos los estudiantes     |

### POST /estudiantes

**Body JSON requerido:**
```json
{
  "nombre":   "Ana García",
  "carrera":  "Ingeniería en Sistemas",
  "semestre": 4
}
```

**Respuesta exitosa (201):**
```json
{
  "mensaje": "Estudiante registrado correctamente",
  "estudiante": {
    "id": 1,
    "nombre": "Ana García",
    "carrera": "Ingeniería en Sistemas",
    "semestre": 4
  }
}
```

### GET /estudiantes

**Respuesta exitosa (200):**
```json
{
  "total": 2,
  "estudiantes": [
    { "id": 1, "nombre": "Ana García", "carrera": "Ingeniería en Sistemas", "semestre": 4 },
    { "id": 2, "nombre": "Luis Ramírez", "carrera": "Contaduría Pública", "semestre": 6 }
  ]
}
```

**Filtro opcional por carrera:**
```
GET /estudiantes?carrera=Sistemas
```

## Conceptos clave que aprenderás

1. **sqlite3.connect()** — abre (o crea) una base de datos SQLite
2. **conn.row_factory = sqlite3.Row** — permite acceder a columnas por nombre en vez de índice
3. **conn.execute(SQL, params)** — ejecuta una consulta con parámetros seguros (evita SQL injection)
4. **conn.commit()** — confirma los cambios en la BD
5. **cursor.lastrowid** — obtiene el ID del último registro insertado
6. **request.get_json()** — lee el body JSON de la petición HTTP
7. **jsonify()** — convierte un dict de Python a respuesta JSON
8. **Códigos HTTP**: 200 OK, 201 Created, 400 Bad Request
