package store

import (
	"github.com/helithumper/feed-star/api/model"
	"github.com/jinzhu/gorm"
)

type ArticleStore struct {
	db *gorm.DB
}

func NewArticleStore(db *gorm.DB) *ArticleStore {
	return &ArticleStore{
		db: db,
	}
}
func (as *ArticleStore) List(offset, limit int) ([]model.Article, int, error) {
	var (
		articles []model.Article
		count    int
	)
	as.db.Model(&articles).Count(&count)
	as.db.Offset(offset).Limit(limit).Find(&articles)
	return articles, count, nil
}
