import json
import spacy
from django.http import JsonResponse

# ჩატვირთე ინგლისური NLP მოდული
nlp = spacy.load("en_core_web_sm")

def simple_bot_logic(user_message):
    """ჩათბოტის პასუხები ინგლისურად"""
    responses = {
        "hello": "Hello! How can I assist you? 😊",
        "how are you": "I'm good, thanks! What about you?",
        "what can you do?": "I'm a chatbot, I can answer your questions!",
        "bye": "Goodbye! Have a great day! 👋",
    }

    user_message = user_message.lower()
    return responses.get(user_message, "Sorry, I didn't understand that. 🤔")

def chatbot_response(request):
    """ჩათბოტის მთავარი ფუნქცია"""
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        # NLP დამუშავება
        doc = nlp(user_message)

        # პასუხის გენერირება
        bot_reply = simple_bot_logic(user_message)

        return JsonResponse({"response": bot_reply})
