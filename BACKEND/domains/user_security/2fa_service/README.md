# 2FA Service (`2fa_service`)

This microservice provides two-factor authentication (2FA) for user login in the SneakRush platform.

## Architecture

- **Hexagonal (Ports & Adapters)**
- **Node.js + Express**
- **Redis** for temporary code storage
- **REST API**
- **SOLID, DRY** principles

## Endpoints

- `POST /api/2fa/send` — Sends a 2FA code
- `POST /api/2fa/validate` — Validates a 2FA code

## Environment Variables

See `.env.example`.

## Run Locally

```bash
npm install
npm start
