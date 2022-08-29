from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from news.api.schema import schema
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Hacker News API",
        default_version="v1",
        description="A RESTful API for Hacker News",
        terms_of_service="https://www.contacts.com/policies/terms/",
        contact=openapi.Contact(email="contact@contacts.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("news.urls")),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    path(
        "doc", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),
    path("redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
