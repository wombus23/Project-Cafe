from django.urls import path
from . import views

urlpatterns = [
    path('',views.chatbot,name="chatbot"),
    path('room/',views.room,name="room"),
    path('chatbot/', views.chatbot_view, name='chatbot_view')
]