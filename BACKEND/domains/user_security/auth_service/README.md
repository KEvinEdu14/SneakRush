# Auth Service - SneakRush

Handles user login, registration, token generation, and authentication for the SneakRush platform.

## Endpoints

- POST `/api/auth/login`
- POST `/api/auth/register`
- POST `/api/auth/refresh`
- POST `/api/auth/logout`

## Environment Variables

- `PORT`
- `JWT_SECRET`
- `DATABASE_URL`

## Run locally

```bash
npm install
npm start
