from django.urls import path
from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.job_list, name='portfolio'),
    path('<int:id>', views.job_detail, name='portfolio'),
]