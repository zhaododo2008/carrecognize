from django.urls import path

from . import views

app_name = 'recognize'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]