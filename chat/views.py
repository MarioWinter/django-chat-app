from django.shortcuts import render

def index(request):
	print(request.method)
	if request.method == 'POST':
		print("Request method is post")
		print(request.POST['textmessage'])
	return render(request, 'chat/index.html')