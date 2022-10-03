from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name="register"),
    path('edit-profile/', views.EditUserView.as_view(), name="edit_info"),
    path('password/', views.ChangePasswordView.as_view(), name="update_password"),
    path('success/', views.PasswordChangeSuccess, name="password_success"),
    path('<int:pk>/profile', views.ProfilePageView.as_view(), name="user_profile"),
    path('<int:pk>/edit-profile', views.EditProfilePageView.as_view(), name="edit_profile"),
    path('create-profile/', views.CreateProfilePageView.as_view(), name="create_profile"),
]