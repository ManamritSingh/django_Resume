from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Lets see if this can work")
    return render(request, 'Resume.html')
