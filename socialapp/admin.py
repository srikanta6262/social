from django.contrib import admin
from socialapp.models import contact,Data
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','msg','postdate']
class DataAdmin(admin.ModelAdmin):
    list_display = ['name','status','location','seen','postdate']



admin.site.register(contact,ContactAdmin)
admin.site.register(Data,DataAdmin)
