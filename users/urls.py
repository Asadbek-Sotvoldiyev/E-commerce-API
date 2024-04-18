from django.urls import path
from .views import LoginApiView, RegisterApiView


app_name = 'users'
urlpatterns = [
    path('login/', LoginApiView.as_view()),
    path('register/', RegisterApiView.as_view()),
]