from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('onsale-items/', views.onSellItemsList, name="/onsale-items"),
]
