from django.urls import path

from . import views

urlpatterns = [
    path('/status', views.StatusView.as_view()),
    path('/file', views.FileUploadView.as_view()),
    path('/hello', views.hello_world),
]