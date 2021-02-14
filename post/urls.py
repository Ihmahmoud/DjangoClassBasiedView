
from django.urls import path
from .import views

app_name = 'post'

urlpatterns = [
    # path('',views.post_list, name='post_list'),
    # path('<int:id>',views.post_details, name='post_detail'),
    
    
    #### for class
    
    path('',views.PostList.as_view(), name='post_list'),
    path('<int:pk>',views.PostDetail.as_view(), name='post_detail'),
]
