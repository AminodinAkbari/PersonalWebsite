from django.shortcuts import render

# Create your views here.
def my_custom_page_404(request , **kwargs):
	return render(request , 'admin/404.html' , {})

handler404 = 'MySettings.views.my_custom_page_404'