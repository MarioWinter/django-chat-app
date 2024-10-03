from django.shortcuts import render
from .models import Chat, Message
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .dummy_data import gadgets

# @login_required(login_url="/login/")

def start_page_view(request):
    return HttpResponse('Startseite vom Backend Django')

def redirect_to_start_page_view(request):
    return redirect('chat-app/', permanent=True)

def single_gadget_view(request, gadget_id):
    return JsonResponse(gadgets[gadget_id])

def index(request):
	print(request.method)
	if request.method == 'POST':
		print(request.POST['textmessage'])
		myChat = Chat.objects.get(id=1)
		Message.objects.create(text=request.POST['textmessage'],chat=myChat, author=request.user, receiver=request.user)
	chatMessages = Message.objects.filter(chat__id=1)
	return render(request, 'chat/index.html', {'messages': chatMessages})

def login_view(request):
	redirect = request.GET.get('next')
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(request.POST.get('redirect'))
		else:
			return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})# boolean variable im HTML
	return render(request, 'auth/login.html', {'redirect':redirect})

def register_view(request):
	redirect = request.GET.get('next')
	print(redirect)
	if request.method == 'POST':
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]
		user = User.objects.create_user(username, email, password)
		user.save()
		return render(request, 'chat/index.html')
	return render(request, 'reg/register.html')