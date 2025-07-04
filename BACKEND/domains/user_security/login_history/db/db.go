package db

import (
	"database/sql"
	"os"

	_ "github.com/lib/pq"
)

var DB *sql.DB

func Init() error {
	connStr := os.Getenv("DATABASE_URL")
	if connStr == "" {
		connStr = "postgres://postgres:supersecret@postgres:5432/sneakrush?sslmode=disable"
	}
	var err error
	DB, err = sql.Open("postgres", connStr)
	if err != nil {
		return err
	}
	return DB.Ping()
}

func CreateTable() error {
	query := `
	CREATE TABLE IF NOT EXISTS login_history (
		id SERIAL PRIMARY KEY,
		user_id INT NOT NULL,
		timestamp TIMESTAMP NOT NULL,
		ip VARCHAR(50)
	)`
	_, err := DB.Exec(query)
	return err
}
