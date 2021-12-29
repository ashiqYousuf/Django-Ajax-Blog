from myapp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('add-new-post/',views.add_post,name='addpost'),
    path('like/',views.like_post,name='like'),
    path('dislike/',views.dislike_post,name='dislike'),
]
