from django.contrib import admin
from .models import AboutMe , Expericence , Education , Skills_Chart , WorkshipSubject , Workship,ContactMe

class AboutMeAdmin(admin.ModelAdmin):
	list_display = [ '__str__' , 'active']

class WorkshipAdmin(admin.ModelAdmin):
	list_display = [ '__str__' , 'image_tag']

# Register your models here.
admin.site.register(AboutMe , AboutMeAdmin)
admin.site.register(Expericence)
admin.site.register(Education)
admin.site.register(Skills_Chart)
admin.site.register(Workship , WorkshipAdmin)
admin.site.register(WorkshipSubject)
admin.site.register(ContactMe)