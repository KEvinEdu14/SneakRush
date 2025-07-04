package handlers

import (
	"encoding/json"
	"login_history/db"
	"login_history/models"
	"net/http"
	"strconv"
	"time"
)

// Estructura del request para crear login
type CreateLoginRequest struct {
	UserID int    `json:"user_id"`
	IP     string `json:"ip"`
}

func CreateLogin(w http.ResponseWriter, r *http.Request) {
	var req CreateLoginRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}
	query := `INSERT INTO login_history (user_id, timestamp, ip) VALUES ($1, $2, $3)`
	_, err := db.DB.Exec(query, req.UserID, time.Now(), req.IP)
	if err != nil {
		http.Error(w, "Failed to register login", http.StatusInternalServerError)
		return
	}
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(map[string]string{"message": "Login registered"})
}

func GetLoginHistory(w http.ResponseWriter, r *http.Request) {
	userIDStr := r.URL.Query().Get("user_id")
	userID, err := strconv.Atoi(userIDStr)
	if err != nil {
		http.Error(w, "Invalid user_id", http.StatusBadRequest)
		return
	}

	rows, err := db.DB.Query(`SELECT id, user_id, timestamp, ip FROM login_history WHERE user_id=$1 ORDER BY timestamp DESC`, userID)
	if err != nil {
		http.Error(w, "Failed to query history", http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var history []models.LoginHistory
	for rows.Next() {
		var l models.LoginHistory
		if err := rows.Scan(&l.ID, &l.UserID, &l.Timestamp, &l.IP); err != nil {
			http.Error(w, "Failed to scan row", http.StatusInternalServerError)
			return
		}
		history = append(history, l)
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(history)
}
