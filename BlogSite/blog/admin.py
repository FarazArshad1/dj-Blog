from django.contrib import admin
from .models import Post

# Register your models here

# Here Post is the model and we are telling the Django Adminstration site that the model is registered in the site using a custom class that iherits from ModlAdmin.
# In this class we can include information about how to display the model on the Adminstartion site and how to interact with it
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title','body']
    prepopulated_fields = {'slug' : ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    
