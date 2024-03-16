from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('transaction/', views.TransactionTypeView.as_view(), name = 'transactiontype'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)