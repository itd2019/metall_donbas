from django.shortcuts import render

# Create your views here.
def Products(request):
    return render(request, 'Products.html', locals())