from django.contrib import admin

# Register your models here.
from .models import Pdf, NewFile, Subscriber, Rubric, Advertising, Category
admin.site.register(Pdf)
admin.site.register(NewFile)
admin.site.register(Subscriber)
admin.site.register(Rubric)
admin.site.register(Advertising)
admin.site.register(Category)