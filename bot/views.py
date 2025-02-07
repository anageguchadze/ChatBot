import json
import spacy
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

# NLP მოდული
nlp = spacy.load("en_core_web_sm")

def simple_bot_logic(user_message):
    """მარტივი ჩათბოტის პასუხები"""
    responses = {
        "hello": "Hello! How can I assist you? 😊",
        "how are you": "I'm good, thanks! What about you?",
        "bye": "Goodbye! Have a great day! 👋",
    }
    return responses.get(user_message.lower(), "Sorry, I didn't understand that. 🤔")

def chat_view(request):
    """ჩათბოტის HTML გვერდი"""
    return render(request, "chat.html")

def chatbot_response(request):
    """ჩათბოტის პასუხი POST მეთოდზე"""
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        bot_reply = simple_bot_logic(user_message)
        return JsonResponse({"response": bot_reply})
    
    # GET მოთხოვნის შემთხვევაში დავაბრუნოთ 405 (Method Not Allowed)
    elif request.method == "GET":
        return HttpResponseNotAllowed("Only POST requests are allowed.")
