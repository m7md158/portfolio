from django.urls import path
from . import views
from . import api

app_name = 'resume'

urlpatterns = [
    path('', views.resume_view, name='resume'),
    ## RestApiFrameWork
    ## CBV
    
    path('works/', api.WorkExperienceList.as_view(), name='resume_api'),
    path('works/<int:id>', api.WorkExperienceDetail.as_view(), name='resume_api'),
    
    path('education/', api.EducationSerializerList.as_view(), name='resume_api'),
    path('education/<int:id>', api.EducationSerializerDetail.as_view(), name='resume_api'),
    
    


]