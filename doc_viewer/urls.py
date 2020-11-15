from django.urls import path
from . import views

app_name = 'doc_viewer'
urlpatterns = [
    path('<int:document_id>/', views.viewer, name='viewer'),
]
