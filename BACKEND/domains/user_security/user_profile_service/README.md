# user_profile_service

Microservicio encargado de manejar operaciones CRUD parciales del perfil de usuario en la plataforma SneakRush.

## 📌 Funcionalidad
- Obtener perfil de usuario por ID
- Actualizar datos del perfil (nombre, teléfono, etc.)

## 🛠️ Tecnologías
- Lenguaje: Python 3.11
- Framework: FastAPI
- Base de datos: PostgreSQL
- ORM: SQLAlchemy
- Principios: SOLID / DRY
- Arquitectura: por capas

## 📁 Estructura
```bash
user_profile_service/
├── main.py
├── Dockerfile
├── requirements.txt
├── .env
├── README.md
├── swagger.yaml
├── config/
├── domain/
├── infrastructure/
├── application/
└── interfaces/
```

## ⚙️ Variables de entorno (.env)
```env
DATABASE_URL=postgresql://sneakrush:sneakrushpass@postgres:5432/sneakrushdb
PORT=4005
```

## 🚀 Instrucciones

### Local
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Docker
```bash
docker compose up --build user_profile_service
```

## 📮 Endpoints principales

| Método | Ruta                  | Descripción                     |
|--------|-----------------------|---------------------------------|
| GET    | /api/profile/{id}     | Obtener perfil de usuario       |
| PUT    | /api/profile/{id}     | Actualizar perfil de usuario    |

## 🧪 Ejemplo cURL
```bash
curl -X GET http://localhost:4005/api/profile/1
```

## 👤 Autor
Equipo SneakRush
