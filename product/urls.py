from django.urls import path
from .schema import schema
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .import views


urlpatterns = [
    path("", csrf_exempt(GraphQLView.as_view(schema=schema, graphiql=True)))
]