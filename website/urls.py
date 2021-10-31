from django.urls import path
from website import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='paginainicial'),
    path('sobre', views.second_page_view, name='sobre'),
    path('contacto', views.third_page_view, name='contacto'),
]