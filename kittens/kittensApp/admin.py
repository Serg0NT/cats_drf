from django.contrib import admin
from .models import Kitten, Breed, User

# admin.site.register(User)
admin.site.register(Kitten)
admin.site.register(Breed)

