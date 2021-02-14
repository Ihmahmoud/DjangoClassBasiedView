from django.shortcuts import render




# Create your views here.


from .models import Post

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# def post_list(request):
#     post_list = Post.objects.all()
#     return render(request , 'post/list.html',{'post_list': post_list})

# def post_details(request,id):
#     pass


class PostList(ListView):
    model = Post




class PostDetail(DetailView):
    model = Post



class PostCreate():
    pass



class PostDelete():
    pass




class PostUpdate():
    pass 



