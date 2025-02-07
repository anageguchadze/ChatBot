from django.urls import path
from .views import chat_view, chatbot_response

urlpatterns = [
    # ჩათბოტის HTML ფორმა
    path("", chat_view, name="chat_view"),
    
    # ჩათბოტის API პასუხი
    path("chatbot/", chatbot_response, name="chatbot_response"),
]
