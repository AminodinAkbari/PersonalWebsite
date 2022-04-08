from django.forms import ModelForm
from .models import ContactMe

class ContactForm(ModelForm):
	class Meta:
		model = ContactMe
		exclude = ["read_or_not"]
		
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class': 'form-control p-4','data-validation-required-message':"Please enter your subject" ,'Placeholder':'Name'})
		self.fields['subject'].widget.attrs.update({'class': 'form-control p-4','data-validation-required-message':"Name can't leave Empty",'Placeholder':'Subject'})
		self.fields['email'].widget.attrs.update({'class': 'form-control p-4','data-validation-required-message':"I need your email for your answer",'Placeholder':'Email'})
		self.fields['text'].widget.attrs.update({'class': 'form-control p-4','data-validation-required-message':"you not write even one word !",'Placeholder':'Text'})

