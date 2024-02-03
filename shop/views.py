# Trong shop/views.py
from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')
def register_view(request):
    # Xử lý đăng ký ở đây nếu cần
    return render(request, 'register.html')