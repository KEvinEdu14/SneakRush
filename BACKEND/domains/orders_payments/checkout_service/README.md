# Checkout Service

Microservicio de checkout (checkout_service) para SneakRush.

## Instalación

1. Copia `.env.example` a `.env` y ajusta variables.
2. Construye la imagen Docker:
   ```bash
   docker build -t kevineduardo14/checkout_service:latest .
   ```
3. Ejecuta:
   ```bash
   docker run --env-file .env -p 8004:8004 kevineduardo14/checkout_service:latest
   ```

## Endpoint

- `POST /checkout/{user_id}?coupon=<code>`
