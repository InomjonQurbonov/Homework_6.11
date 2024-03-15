from django.urls import path

from .views import pupils_list, pupils_detail,create_pupil,edit_pupil,delete_pupil

urlpatterns = [
    path('pupils', pupils_list, name='pupils_list'),
    path('pupils/<int:pk>/', pupils_detail, name='pupil_info'),
    path('add/', create_pupil, name='add_pupil'),
    path('edit/<int:pk>/', edit_pupil, name='edit_pupil'),
    path('delete/<int:pk>/',delete_pupil, name='delete_pupil')
]