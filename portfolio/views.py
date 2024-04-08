from django.shortcuts import render
from .models import Project
from .forms import ContactForm


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    projects = Project.objects.all()
    context = {
        'projects': projects,
        'form': form
    }

    return render(request, 'index.html', context)
