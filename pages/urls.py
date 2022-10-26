from django.urls import path
from .views import HomePageView, AboutPageView, DownloadImgView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('', HomePageView.as_view(), name = 'home'),
    path('download-img/<int:pk>/', DownloadImgView.as_view(), name = 'img'),
]