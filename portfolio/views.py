from django.shortcuts import render
from .models import Project, Contact
from .forms import ContactForm


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    form = ContactForm()
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects, 'form': form})
