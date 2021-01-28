from django.urls import path

from quickstart import views

app_name = 'quickstart'


urlpatterns = [
    path('create/', views.endpoint, name="create")
]