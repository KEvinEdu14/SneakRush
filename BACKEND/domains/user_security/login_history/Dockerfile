FROM golang:1.20 as builder

WORKDIR /app
COPY . .

RUN go mod tidy
ENV CGO_ENABLED=0
ENV GOOS=linux
RUN go build -o login-history main.go

FROM debian:bullseye-slim
WORKDIR /app
COPY --from=builder /app/login-history .
COPY .env .env

EXPOSE 8080

CMD ["./login-history"]
