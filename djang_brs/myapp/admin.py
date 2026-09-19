"""
Developed by MASA
All Rights Reserved.
"""

from django.contrib import admin
from .models import Bus, User, Book

admin.site.register(Bus)
admin.site.register(User)
admin.site.register(Book)
