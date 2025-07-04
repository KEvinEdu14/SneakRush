# SneakRush Login History Service (REST)

REST API en Go para registrar y consultar historial de logins.

## Endpoints

- POST `/logins` — Registra un login
- GET `/logins?user_id=1` — Consulta historial de un usuario

## Docker

docker build -t login-history .
docker run -p 8080:8080 --env-file .env login-history
