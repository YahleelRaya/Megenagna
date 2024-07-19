from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def retrieve(request):
    template= loader.get_template('Employer_registration/Employer_registration.html')
    return HttpResponse(template.render())

@csrf_exempt
def submit(request):
    if request.method == 'POST':
        fname = request.POST.get('Fname')
        lname = request.POST.get('Lname')
        age = request.POST.get('Age')
        return HttpResponse(f'Name:{fname}')

