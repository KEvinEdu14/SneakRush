# User Service

Microservicio de perfil de usuario (user_service) para SneakRush.

## Instalación

1. Copia `.env.example` a `.env` y completa las variables.
2. Construye la imagen:
   ```
   docker build -t sneakrush-user-service .
   ```
3. Levanta con Docker Compose o directamente:
   ```
   docker run --env-file .env -p 8000:8000 sneakrush-user-service
   ```

## Endpoints

- `POST /users`
- `GET /users`
- `GET /users/{user_id}`
- `PUT /users/{user_id}`
- `DELETE /users/{user_id}`

## Testing

```
pytest
```
