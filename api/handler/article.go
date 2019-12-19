package handler

import (
	"errors"
	"net/http"

	_ "github.com/helithumper/feed-star/api/model"
	"github.com/labstack/echo/v4"
)

func (h *Handler) ListArticles(c echo.Context) error {
	return c.String(http.StatusOK, "Hello")
}
