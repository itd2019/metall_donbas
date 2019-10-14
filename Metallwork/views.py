from django.shortcuts import render

# Create your views here.
def Metallwork(request):
    return render(request, 'Metallwork.html', locals())