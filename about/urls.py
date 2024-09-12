from django.urls import path
from . import views
from . import api
app_name = 'about'

urlpatterns = [
    path('', views.about_view, name='about'),
    # restframework
    # CBV
    path('api/', api.SkillsList.as_view(), name='about_api'),
    path('api/<int:id>', api.SkillsDetail.as_view(), name='about_api_detail'),
 
]