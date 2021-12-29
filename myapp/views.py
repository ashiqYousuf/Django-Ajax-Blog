from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request , 'myapp/home.html',{'posts':posts})



def add_post(request):
    if request.method=='POST':
        fm=PostForm(request.POST)
        if fm.is_valid():
            title=fm.cleaned_data['title']
            title=title.lower()
            stringlist=title.split(' ')
            slug="-".join([str(e) for e in stringlist])
            Post(title=title , slug=slug).save()
            messages.success(request , 'Post added Successfully')
            return HttpResponseRedirect('/')
    else:
        fm=PostForm()
    return render(request , 'myapp/forms.html',{'form':fm})




def like_post(request):
    if request.method=='GET':
        id=request.GET.get('id')
        print(id)
        post=Post.objects.get(pk=id)
        post.likes+=1
        post.save()
        return JsonResponse({'likes':post.likes})

def dislike_post(request):
    if request.method=='GET':
        id=request.GET.get('id')
        print(id)
        post=Post.objects.get(slug=id)
        post.dislikes+=1
        post.save()
        return JsonResponse({'dislikes':post.dislikes})
