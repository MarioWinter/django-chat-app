from django.urls import path
from .views import index, login_view, register_view, start_page_view, single_gadget_view, single_gadget_init_view, GadgetView

urlpatterns = [
    path('', start_page_view),
    path('chat/', index),
    path('login/', login_view),
    path('register/', register_view),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_init_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url")
]