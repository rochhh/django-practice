from django.shortcuts import render,redirect
from .forms import PostForm
# Create your views here.

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.save()
        return redirect("/")
    else:
        form = PostForm()
      
    return render(request,"posts/new.html", {"form":form} )