from django.urls import path
from .views import themes_list,theme_detail,create_theme,edit_theme,delete_theme

urlpatterns = [
    path('',themes_list,name='themes_list'),
    path('<int:pk>/',theme_detail,name='theme_detail'),
    path('add/',create_theme,name='add_theme'),
    path('edit/<int:pk>/', edit_theme, name='edit_theme'),
    path('delete/<int:pk>/', delete_theme, name='delete_theme')
]