package article

import (
	"github.com/helithumper/feed-star/api/model"
)

type Store interface {
	List(offset, limit int) ([]model.Article, int, error)
}
