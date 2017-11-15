from django.shortcuts import render, render_to_response, get_object_or_404
from blog import models

# Create your views here.
def post_list(request):
    return render(request,'blog/post_list.html')

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })