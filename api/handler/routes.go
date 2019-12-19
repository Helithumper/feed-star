package handler

import (
	"github.com/labstack/echo"
)

func (h *Handler) Register(v1 *echo.Group) {
	articles := v1.Group("/articles")
	articles.GET("", h.Feed)
}
