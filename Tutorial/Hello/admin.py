from django.contrib import admin

from Hello.models import Contact, User

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)