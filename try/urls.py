from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexAll, name="indexAll"),
    path("check/<str:user_id>", views.check, name="check"),
    path("delete/<str:user_id>",views.deleteID, name="delete"),
    path("delete",views.delete, name="delete"),
    path("edit/<str:user_id>", views.edit, name="edit"),
]
