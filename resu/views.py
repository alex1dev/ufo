
from django.shortcuts import render, redirect
from resu.forms import ContactForm
# Create your views here.
from django.core.mail import send_mail,  BadHeaderError


def index(request):
	form = ContactForm(request.POST)

	if request.method == 'POST':
		
		
		if form.is_valid():
			subject = form.cleaned_data['subject']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject,message, email, ['admin@admin.py'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('resu/index')

	return render(request, "resu/index.html", {'form' : form})