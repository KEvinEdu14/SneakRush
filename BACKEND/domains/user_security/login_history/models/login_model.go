package models

import "time"

type LoginHistory struct {
	ID        int       `json:"id"`
	UserID    int       `json:"user_id"`
	Timestamp time.Time `json:"timestamp"`
	IP        string    `json:"ip"`
}
