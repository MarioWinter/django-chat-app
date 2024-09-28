from django.shortcuts import render
from .models import Chat, Message

def index(request):
	print(request.method)
	if request.method == 'POST':
		print(request.POST['textmessage'])
		myChat = Chat.objects.get(id=1)
		Message.objects.create(text=request.POST['textmessage'],chat=myChat, author=request.user, receiver=request.user)
	return render(request, 'chat/index.html')