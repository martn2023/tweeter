from django.urls import path
from . import views

app_name = 'public_messages'

urlpatterns = [
    path('create/', views.create_post, name='create_post'),

]
