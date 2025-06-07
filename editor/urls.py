# editor/urls.py

from django.urls import path
from . import views

app_name = 'editor'

urlpatterns = [
    path('', views.editor_view, name='editor_page'),
    path('api/process/', views.api_process_text, name='api_process_text'),
    path('download/docx/', views.download_docx, name='download_docx'), # Yeni DOCX indirme URL'si
    # path('download/txt/', views.download_txt, name='download_txt'), # TXT indirme JS'te halledildi
]