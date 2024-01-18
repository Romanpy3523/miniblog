from django.shortcuts import render
from django.views.generic.base import View
from .models import Post
# Create your views here.

class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/index.html', {'post_list': posts})
    

class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})    