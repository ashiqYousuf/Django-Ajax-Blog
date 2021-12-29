from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','date','likes','dislikes','slug']
    list_editable=['likes','dislikes','slug']
    prepopulated_fields={'slug':('title',)}