from django.contrib import admin

# Register your models here.

from carl.models import Comediante, Show

#admin.site.register(Comediante)

# Define the admin class
class ComedianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'especialidad')

class ShowAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora', 'lugar')
# Register the admin class with the associated model
admin.site.register(Comediante, ComedianteAdmin)
admin.site.register(Show, ShowAdmin)
