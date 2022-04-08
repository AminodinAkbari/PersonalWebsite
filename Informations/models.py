from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.html import format_html

# Create your models here.
class AboutMe(models.Model):
	name   = models.CharField(max_length = 200)
	titles = models.TextField()
	text   = RichTextField()
	personal_informations = models.TextField()
	CV = models.URLField(blank = True , null=True)
	active = models.BooleanField()

	def __str__(self):
		return f'My Name Is {self.name} ! I Think This Can Be Show In Index :) '

class Expericence(models.Model):
	ways_to_learn = (
	('SelfStudy','SelfStudy'),
	('By Master','By Master')
	)
	title 		= models.CharField(max_length = 300)
	how_learned = models.CharField(choices = ways_to_learn , max_length=12)
	description = models.TextField()

	def __str__(self):
		return self.title

class Education(models.Model):
	title = models.CharField(max_length = 300)
	university = models.CharField(max_length = 200)
	date_start = models.DateTimeField()
	date_end = models.DateTimeField()
	description = models.TextField()

	def __str__(self):
		return self.title

class Skills_Chart(models.Model):
	Bootstrap_classes_for_colors = (
	('bg-primary','WebTheme'),
	('bg-danger','Red'),
	('bg-success','Green'),
	('bg-warning','Yellow'),
	('bg-info','Blue'),
	)
	title = models.CharField(max_length = 250)
	percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
	color = models.CharField(max_length = 10 , choices = Bootstrap_classes_for_colors)

	def __str__(self):
		return self.title

class WorkshipSubject(models.Model):
	subject = models.CharField(max_length = 50)

	def __str__(self):
		return self.subject

class Workship(models.Model):
	Workship_subject = models.ForeignKey(WorkshipSubject , on_delete = models.PROTECT , blank=True , null=True)
	title = models.URLField(max_length=530)
	screen_shot = models.ImageField(blank=True , null=True,upload_to = 'screen_shots/' , default = 'static/freelancer-portfolio-template.jpg')
	short_description = models.CharField(max_length = 250)

	def image_tag(self):
		if self.screen_shot:
			return format_html(f'<img src="{self.screen_shot.url}" / style="width:70px;">')
		else:
			return ''

	def __str__(self):
		return f'{self.title[8:25]} ...'

class ContactMe(models.Model):
	name = models.CharField(max_length = 250)
	subject = models.CharField(max_length = 350)
	email = models.EmailField()
	text = models.TextField()
	read_or_not = models.BooleanField(default=False)

	def __str__(self):
		return self.subject