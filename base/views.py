from django.shortcuts import render
from django.http import JsonResponse
from .qanoonbot import QanoonBot
def chatbot(request):
    return render(request,'chatbot.html')
def room(request):
    return render(request,'room.html')
def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get("user_message", "")
        chatbot = QanoonBot
        response = chatbot.process_message(user_message)
        return JsonResponse({"response": response})

    return render(request, "chatbot.html")
