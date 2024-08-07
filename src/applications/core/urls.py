from django.urls import path
from .views import UserLoginView, UserRegistrationView, UserView, UserFilter

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('user/', UserView.as_view(), name="current_user"),
    path('filter/', UserFilter, name='user_filter')
]