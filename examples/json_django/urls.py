from django.urls import path

from .views import ReadJsonView

urlpatterns = [
    path('', ReadJsonView.as_view(), name='readJson')
]
