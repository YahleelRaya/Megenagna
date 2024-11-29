from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from .db_connection import db
from .models import users_collection
from .forms import WorkerForm
from .forms import EmployerForm
# Create your views here.
#def retrieveEmployer(request):
   # template= loader.get_template('Employer_registration/Employer_registration.html')
   # return HttpResponse(template.render())
worker_collection = db['Worker_Coll']
employer_collection = db['Employer_Coll']
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

  
def add_user(request, user_type):
    if request.method == 'POST':
        form = WorkerForm(request.POST, request.FILES) if user_type == 'worker' else EmployerForm(request.POST, request.FILES)
        
        if form.is_valid():
            user_data = form.cleaned_data

            # Handle file uploads
            for file_field in ['government_id', 'cv', 'picture', 'reference_id']:
                if file_field in request.FILES:
                    user_data[file_field] = request.FILES[file_field].name

            # Choose collection based on user type
            collection = worker_collection if user_type == 'worker' else employer_collection
            collection.insert_one(user_data)
            return HttpResponse("New user added")
        else:
            return HttpResponse("Form is not valid")
    else:
        form = WorkerForm() if user_type == 'worker' else EmployerForm()
        template_name = 'Worker_registration/Worker_registration.html' if user_type == 'worker' else 'Employer_registration/Employer_registration.html'
        return render(request,template_name, {'form': form})


   


def get_all_users(request):
    users=users_collection.find()
    return HttpResponse(users)
