from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

# Create your views here.
#def retrieveEmployer(request):
   # template= loader.get_template('Employer_registration/Employer_registration.html')
   # return HttpResponse(template.render())
def retrieve(request, user_type):
    if user_type == 'employer':
        template_name = 'Employer_registration/Employer_registration.html'
    elif user_type == 'worker':
        template_name = 'Worker_registration/Worker_registration.html'
    else:
        return HttpResponseBadRequest("Invalid user type specified.")
    context = {
        'title': f'{user_type.capitalize()} Registration',
        'message': f'Welcome to the {user_type.capitalize()} Registration Page',
    }
    return render(request, template_name, context)
@csrf_exempt
def submit(request):
    if request.method == 'POST':
        fname = request.POST.get('Fname')
        lname = request.POST.get('Lname')
        age = request.POST.get('Age')
        return HttpResponse(f'Name:{fname}')

