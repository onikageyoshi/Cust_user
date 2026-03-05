from django.urls import path
from .views import UserDetailsView,CreateUserView

urlpatterns = [
    path("users/<int:pk>/", UserDetailsView.as_view(), name="user-detail"),
    path("users/", CreateUserView.as_view(), name="create-user"),
]