from datetime import datetime
from django.shortcuts import render
from posts.models import Post
# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html" ,                 
                {"currentTime" : datetime.now() , 
                 "posts" : Post.objects.all(),
                 "numPosts" : Post.objects.count()
                }) 