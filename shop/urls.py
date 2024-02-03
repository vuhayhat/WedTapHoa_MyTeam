# Trong shop/urls.py
from django.urls import path
from .views import login_view  # Đổi tên import để sử dụng login_view
from .views import register_view
urlpatterns = [
    path('', login_view, name='login'),  # Sử dụng login_view thay vì your_default_view
    path('login/', login_view, name='login'),  # Giữ lại nếu cần thiết
    path('', register_view, name='register'),
    path('register/', register_view, name='register'),

    # Các đường dẫn khác nếu có
]
