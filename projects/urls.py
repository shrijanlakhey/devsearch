from django.urls import path
from . import views
urlpatterns = [
    path('',views.projects, name="projects"),  #http://127.0.0.1:8000/(root doamin) mah jada projects.html load hunxa
    path('project/<str:pk>/', views.project, name="project"),
]