package main

import (
	"log"
	"net/http"
	"os"

	"login_history/db"
	"login_history/handlers"

	"github.com/joho/godotenv"
)

func main() {
	_ = godotenv.Load(".env")

	if err := db.Init(); err != nil {
		log.Fatalf("Cannot connect to DB: %v", err)
	}
	if err := db.CreateTable(); err != nil {
		log.Fatalf("Cannot create table: %v", err)
	}

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	http.HandleFunc("/logins", func(w http.ResponseWriter, r *http.Request) {
		switch r.Method {
		case http.MethodPost:
			handlers.CreateLogin(w, r)
		case http.MethodGet:
			handlers.GetLoginHistory(w, r)
		default:
			http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
		}
	})

	log.Printf("REST API server running on :%s", port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}
