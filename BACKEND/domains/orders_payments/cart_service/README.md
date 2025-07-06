# Cart Service

Microservicio de carrito (cart_service) para SneakRush.

## Instalación

1. Copia `.env.example` a `.env` y completa las variables.
2. Instala dependencias:
   ```
   npm install
   ```
3. Arranca el servicio:
   ```
   npm start
   ```

## Endpoints

- `POST   /cart/{userId}/items`
- `GET    /cart/{userId}/items`
- `PUT    /cart/{userId}/items/{itemId}`
- `DELETE /cart/{userId}/items/{itemId}`
- `DELETE /cart/{userId}`

## Docker

Construye y corre con Docker:
```
docker build -t kevineduardo14/cart_service:latest .
docker run --env-file .env -p 4001:4001 kevineduardo14/cart_service:latest
```
