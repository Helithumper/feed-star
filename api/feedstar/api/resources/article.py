from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from feedstar.models import Article
from feedstar.extensions import ma, db
from feedstar.commons.pagination import paginate


class ArticleSchema(ma.ModelSchema):

    # id = ma.Int(dump_only=True)
    # password = ma.String(load_only=True, required=True)

    class Meta:
        model = Article
        sqla_session = db.session


class ArticleResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      parameters:
        - in: path
          name: article_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  article: ArticleSchema
        404:
          description: article does not exists
      security: []
    put:
      tags:
        - api
      parameters:
        - in: path
          name: article_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              ArticleSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: article updated
                  article: ArticleSchema
        404:
          description: article does not exists
    delete:
      tags:
        - api
      parameters:
        - in: path
          name: article_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: article deleted
        404:
          description: article does not exists
    """
    # method_decorators = [jwt_required]

    def get(self, article_id):
        schema = ArticleSchema()
        article = Article.query.get_or_404(article_id)
        return {"article": schema.dump(article).data}

    @jwt_required
    def put(self, article_id):
        schema = ArticleSchema(partial=True)
        article = Article.query.get_or_404(article_id)
        article, errors = schema.load(request.json, instance=article)
        if errors:
            return errors, 422

        db.session.commit()

        return {"msg": "article updated", "article": schema.dump(article).data}

    @jwt_required
    def delete(self, article_id):
        article = Article.query.get_or_404(article_id)
        db.session.delete(article)
        db.session.commit()

        return {"msg": "article deleted"}


class ArticleList(Resource):
    """Creation and get_all

    ---
    get:
      description: Get all articles in a paginated format
      tags:
        - api
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/ArticleSchema'
      security: []
    post:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              ArticleSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: article created
                  article: ArticleSchema
    """

    def get(self):
        schema = ArticleSchema(many=True)
        query = Article.query
        return paginate(query, schema)

    @jwt_required
    def post(self):
        schema = ArticleSchema()
        article, errors = schema.load(request.json)
        if errors:
            return errors, 422

        db.session.add(article)
        db.session.commit()

        return {"msg": "article created", "article": schema.dump(article).data}, 201
