

from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_status, name='review_status'),
]
