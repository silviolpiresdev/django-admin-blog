from django.db import models
from mdeditor.widgets import MDEditorWidget
from django.contrib import admin
from .models import Post, Tecnologia
from django.contrib.auth.models import User

admin.site.unregister(User)

class PostInLine(admin.StackedInline):
    model = Post
    
    
class UserAdmin(admin.ModelAdmin):
    inlines = [
        PostInLine, 
               ]


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    
    
    
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tecnologia)
# Register your models here.
