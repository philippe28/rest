from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Produto

# Register your models here

"""
@admin.register(Produto)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('cpu', 'memoria', 'disco', 'so', 'preco', 'provedores')
"""


admin.site.register(Produto)
