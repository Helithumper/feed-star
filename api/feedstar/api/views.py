from flask import Blueprint, current_app
from flask_restful import Api

from feedstar.extensions import apispec
from feedstar.api.resources import ArticleResource, ArticleList
# from feedstar.api.resources.user import UserSchema
from feedstar.api.resources.article import ArticleSchema


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(ArticleResource, '/article/<int:article_id>')
api.add_resource(ArticleList, '/article')


@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("ArticleSchema", schema=ArticleSchema)
    apispec.spec.path(view=ArticleResource, app=current_app)
    apispec.spec.path(view=ArticleList, app=current_app)
