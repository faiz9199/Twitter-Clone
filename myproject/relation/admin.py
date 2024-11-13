from django.contrib import admin
from .models import Author, Profile, Book

# Admin class for Author model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']

# Admin class for Profile model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['author', 'bio', 'website']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_date', 'author']

# Register both models with the admin site
admin.site.register(Author, AuthorAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Book, BookAdmin)
