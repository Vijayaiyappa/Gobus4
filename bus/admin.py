from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Kodagu_town)
admin.site.register(models.Napoklu)
admin.site.register(models.somarpet)
admin.site.register(models.Madikeri)
admin.site.register(models.madikeri2)
admin.site.register(models.virajpet)
admin.site.register(models.kutta)
admin.site.register(models.gonikoppal)
admin.site.register(models.ponnampet)


admin.site.register(models.corrected_data_by_user)
admin.site.register(models.images)#data_given_by_user
admin.site.register(models.data_given_by_user)


admin.site.site_header="GO bus"
