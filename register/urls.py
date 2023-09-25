from django.urls import path

from .views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('list/', UserDetail.as_view(), name='user_detail')
]
