# Trong shop/urls.py
from django.urls import path
from .views import login_view  # Đổi tên import để sử dụng login_view

urlpatterns = [
    path('', login_view, name='login'),  # Sử dụng login_view thay vì your_default_view
    path('login/', login_view, name='login'),  # Giữ lại nếu cần thiết
    # Các đường dẫn khác nếu có
]
