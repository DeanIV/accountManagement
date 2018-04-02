from django.contrib import admin

# Register your models here.
# admin.site.register(MODEL_NAME)
# see : https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site   -- for admin model setup

from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
