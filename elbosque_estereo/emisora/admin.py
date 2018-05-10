from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Module)
admin.site.register(Role_Module)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Program)
admin.site.register(Schedule_program)