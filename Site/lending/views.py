from django.shortcuts import render
from .models import Blog

def index(request):
    form = Blog.objects.order_by('-date')[:5]
    return render(request, 'index.html',{'form':form})