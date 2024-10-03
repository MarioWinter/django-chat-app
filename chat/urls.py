from django.urls import path
from .views import index, login_view, register_view, start_page_view, single_gadget_view

urlpatterns = [
    path('', start_page_view),
    path('chat/', index),
    path('login/', login_view),
    path('register/', register_view),
    path('gadget/', single_gadget_view)
]