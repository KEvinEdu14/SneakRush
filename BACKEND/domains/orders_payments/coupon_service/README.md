# Coupon Service

Microservicio de validación de cupones (coupon_service) para SneakRush.

## Instalación

1. Copia `.env.example` a `.env` y ajusta la URL de Postgres.
2. Construye la imagen:
   ```bash
   docker build -t kevineduardo14/coupon_service:latest .
   ```
3. Ejecuta:
   ```bash
   docker run --env-file .env -p 4008:8002 kevineduardo14/coupon_service:latest
   ```

## Endpoint

- `GET /coupons/{code}/validate`
