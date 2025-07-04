# Notification Service (`notification_service`)

Microservicio encargado de enviar correos y SMS para la plataforma **SneakRush**.


| Dominio | `orders_payments` |
| Lenguaje | Node.js (v20) |
| Base de datos | MongoDB 
| Síncrono | REST `POST /send` |
| Asíncrono | Redis Pub/Sub 
| Patrones | Clean / Hexagonal · SOLID · DRY |

## Endpoints

 `/send` 
## Variables de entorno

Ver `.env.example`.

## Correr localmente

```bash
npm install
npm start
