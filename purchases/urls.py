from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("purchases/", views.PurchaseListView.as_view(), name="purchase-list"),
    path(
        "purchases/<int:pk>/",
        views.PurchaseDetailView.as_view(),
        name="purchase-detail",
    ),
    path(
        "purchases/create/", views.PurchaseCreateView.as_view(), name="purchase-create"
    ),
]
