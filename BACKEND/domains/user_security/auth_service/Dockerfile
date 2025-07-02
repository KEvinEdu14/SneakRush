FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 8000
# Healthcheck que el ALB usará
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s \
  CMD wget --quiet --tries=1 --spider http://localhost:8000/health || exit 1
CMD ["npm", "start"]
