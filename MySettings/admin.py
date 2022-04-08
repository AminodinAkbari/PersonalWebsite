from django.contrib import admin
from .models import SiteSetting , Social
# Register your models here.

class SiteSettingAdmin(admin.ModelAdmin):
	list_display = ['logo_part1' , 'logo_part2','active']

class SocialAdmin(admin.ModelAdmin):
	list_display = ['__str__' , 'icon_tag']

admin.site.register(SiteSetting , SiteSettingAdmin)
admin.site.register(Social , SocialAdmin)