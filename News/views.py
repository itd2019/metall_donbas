from django.shortcuts import render

# Create your views here.
def News(request):
    return render(request, 'News.html', locals())