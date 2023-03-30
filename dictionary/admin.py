from django.contrib import admin
from .models import *
# Register your models here.
class DictionaryAdmin(admin.ModelAdmin):
    list_display = ['input_word','output_word']

admin.site.register(DictionaryEntry,DictionaryAdmin)