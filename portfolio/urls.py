from django.urls import path
from . import views
from . import api

app_name = 'portfolio'

urlpatterns = [
    path('', views.job_list, name='portfolio'),
    path('<int:id>', views.job_detail, name='portfolio'),
    
    ## CBV
    path('jobs', api.JobSerializerList.as_view(), name='jobs'),
    path('jobs/<int:id>', api.JobSerializerDetail.as_view(), name='jobs_detail'),
    
    path('category', api.CategorySerializerList.as_view(), name='category'),
    path('category/<int:id>', api.CategorySerializerDetail.as_view(), name='category_detail'),
    
    
]