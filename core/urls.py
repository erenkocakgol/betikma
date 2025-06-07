from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('hakkimizda/', views.about_view, name='about'),
    path('hizmetler/', views.services_view, name='services'),
    path('iletisim/', views.contact_view, name='contact'),
    path('gizlilik-politikasi/', views.privacy_policy_view, name='privacy_policy'),
    path('kullanim-kosullari/', views.terms_of_service_view, name='terms_of_service'),
    path('destek/', views.support_view, name='support'),
]
