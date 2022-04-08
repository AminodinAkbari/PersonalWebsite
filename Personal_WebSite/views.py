from django.views.generic import ListView , DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import  reverse_lazy
from django.contrib import messages

from Informations.models import AboutMe , Expericence , Education , Skills_Chart , Workship , WorkshipSubject
from Informations.forms import ContactForm
from Informations.models import ContactMe
from MySettings.models import SiteSetting , Social


class Index(FormView):
	template_name = 'index.html'
	model = AboutMe
	form_class = ContactForm

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)

		Me = AboutMe.objects.filter(active = True).first()
		context['AboutMe'] = Me
		context['PersonalInfos'] = Me.personal_informations.split(',')
		context['MyExpericence'] = Expericence.objects.all()
		context['MyEducation'] = Education.objects.all()
		context['SkillsChart'] = Skills_Chart.objects.all()
		context['Workship'] = Workship.objects.all()
		context['WorkshipSubject'] = WorkshipSubject.objects.all()
		context['SiteSettings'] = SiteSetting.objects.filter(active = True).first()
		context['Social'] = Social.objects.all()
		
		return context

	
	def get_success_url(self):
		messages.success(self.request, "I Got You'r Message ☻")
		return reverse_lazy('Home')

	


