from django.shortcuts import render
from .models import Chat, Message
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .dummy_data import gadgets
from django.utils.text import slugify
from django.urls import reverse
import json

# @login_required(login_url="/login/")

def start_page_view(request):
    return HttpResponse('Startseite vom Backend Django')

def redirect_to_start_page_view(request):
    return redirect('chat-app/', permanent=True)

def single_gadget_init_view(request, gadget_id):
	if len(gadgets) > gadget_id:
		new_slug = slugify(gadgets[gadget_id]["name"])
		new_url = reverse("gadget_slug_url", args=[new_slug])
		return redirect(new_url)
	return HttpResponseNotFound('not found by me')


def single_gadget_view(request, gadget_slug=""):
    if request.method == "GET":
        gadget_match = None
        for gedget in gadgets:
            if slugify(gedget["name"]) == gadget_slug:
                gadget_match = gedget
        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data["test"]}")
            return JsonResponse({"response" : "Das war was!"})
        except:
            return JsonResponse({"response" : "Das war nix!"})






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