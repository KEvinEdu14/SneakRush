FROM node:20.12.2-slim

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install --omit=dev && npm cache clean --force

COPY . .

USER appuser

EXPOSE 4002

CMD ["npm", "start"]
