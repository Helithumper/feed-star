package handler

import (
	"github.com/helithumper/feed-star/api/article"
)

type Handler struct {
	articleStore article.Store
}

func NewHandler(as article.Store) *Handler {
	return &Handler{
		articleStore: as,
	}
}
