from django.shortcuts import render

# Create your views here.
def Clients(request):
    return render(request, 'Clients.html', locals())