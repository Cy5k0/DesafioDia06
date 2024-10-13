from django.urls import path
from . import views

urlpatterns = [
    # path("app1/", views.vista_app1, name="app1"),
    path("app2/", views.mostrar_lista, name="app2"),
]
