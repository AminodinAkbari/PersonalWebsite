from django.db import models
from django.utils.html import format_html

# Create your models here.
class SiteSetting(models.Model):
	logo_part1 = models.CharField(max_length=10 , default='LOGO')
	logo_part2 = models.CharField(max_length=10 , blank = True , null = True)
	footer_text = models.TextField()
	active = models.BooleanField()

	# def __str__(self):
	# 	return self.active

class Social(models.Model):
	icon = models.CharField(max_length = 80)
	link = models.CharField(max_length = 500)

	def icon_tag(self):
		if self.icon:
			return format_html(f'<h1 class = "{self.icon}"></h1>')
		else:
			return ''

	def __str__(self):
		return self.link[:25]