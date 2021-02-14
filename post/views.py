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
    model = Post    ## in template {object_list, post_list}
    #context_object_name = 'all_posts'
    ordering = ['-created_at']
    #queryset = Post.objects.filter(active=True)
    #template_name = 'post/test.html'
    

    ##method 
    def get_queryset(self): ## will override of attribute for queryset = Post.objects.filter(active=True)
        return Post.objects.filter(active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["CheckTheName"] = "Ihmahmoud"
        return context
    


class PostDetail(DetailView):
    model = Post



class PostCreate():
    pass



class PostDelete():
    pass




class PostUpdate():
    pass 



