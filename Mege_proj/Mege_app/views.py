from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from db_connection import db
from .models import users_collection
from .forms import WorkerForm
# Create your views here.
#def retrieveEmployer(request):
   # template= loader.get_template('Employer_registration/Employer_registration.html')
   # return HttpResponse(template.render())
users_collection = db['Worker_Coll']
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
  
def add_user(request):
     if request.method == 'POST':
        form = WorkerForm(request.POST, request.FILES)
        if form.is_valid():
            worker_data = form.cleaned_data

            # Handle file uploads
            if 'government_id' in request.FILES:
                worker_data['government_id'] = request.FILES['government_id'].name
            if 'cv' in request.FILES:
                worker_data['cv'] = request.FILES['cv'].name
            if 'picture' in request.FILES:
                worker_data['picture'] = request.FILES['picture'].name
            if 'reference_id' in request.FILES:
                worker_data['reference_id'] = request.FILES['reference_id'].name

            # Insert data into MongoDB
            users_collection.insert_one(worker_data)
            return HttpResponse("New user added")
        else:
            return HttpResponse("Form is not valid")
     else:
        form=WorkerForm
        return render(request,)
         

   


def get_all_users(request):
    users=users_collection.find()
    return HttpResponse(users)
