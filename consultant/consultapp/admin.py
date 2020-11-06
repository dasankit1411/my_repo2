from django.contrib import admin
from consultapp.models import *
# Register your models here.
class OrganisationAdmin(admin.ModelAdmin):
    list_display=['name','type','location','requirement','contact']

class ExpertAdmin(admin.ModelAdmin):
    list_display=['name','skill','experience','contact']

    
admin.site.register(Organisation,OrganisationAdmin)
admin.site.register(Expert,ExpertAdmin)
