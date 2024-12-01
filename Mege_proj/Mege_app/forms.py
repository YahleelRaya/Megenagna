from django import forms 

class WorkerForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    EDUCATION_CHOICES = [
        ('LessThanHS', 'Less Than High School'),
        ('Highschool', 'Highschool'),
        ('Tradeschool', 'Trade School'),
        ('University', 'University'),
    ]

    JOB_TYPE_CHOICES = [
        ('Cooking', 'Cooking'),
        ('Cleaning', 'Cleaning'),
        ('Babysitting', 'Babysitting'),
        ('Other', 'Other'),
    ]

    SCHEDULE_CHOICES = [
        ('LiveIn', 'Live In'),
        ('Commute', 'Commute'),
    ]

    EXPERIENCE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    LANGUAGE_CHOICES = [
        ('Amharic', 'Amharic'),
        ('Oromigna', 'Oromigna'),
        ('Tigrigna', 'Tigrigna'),
        ('Somaligna', 'Somaligna'),
        ('Sidamigna', 'Sidamigna'),
    ]

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField(required=False)
    education_history = forms.ChoiceField(choices=EDUCATION_CHOICES)
    government_id = forms.FileField()
    cv = forms.FileField(required=False)
    picture = forms.FileField(required=False)
    job_type = forms.ChoiceField(choices=JOB_TYPE_CHOICES)
    other_job = forms.CharField(max_length=50, required=False)
    schedule = forms.ChoiceField(choices=SCHEDULE_CHOICES)
    experience = forms.ChoiceField(choices=EXPERIENCE_CHOICES)
    employer_name = forms.CharField(max_length=100, required=False)
    employer_phone = forms.CharField(max_length=15, required=False)
    employment_length = forms.CharField(max_length=50, required=False)
    languages = forms.MultipleChoiceField(choices=LANGUAGE_CHOICES)
    other_language = forms.CharField(max_length=50, required=False)
    reference_name = forms.CharField(max_length=100)
    reference_phone = forms.CharField(max_length=15)
    reference_email = forms.EmailField(required=False)
    reference_address = forms.CharField(max_length=200)
    reference_id = forms.FileField()
    agreement_signature = forms.CharField(max_length=100)

    class EmployerForm(forms.Form):
    
     GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    JOB_TYPE_CHOICES = [
        ('Cooking', 'Cooking'),
        ('Cleaning', 'Cleaning'),
        ('Babysitting', 'Babysitting'),
    ]
    
    SCHEDULE_CHOICES = [
        ('LiveIn', 'Live In'),
        ('Commute', 'Commute'),
    ]
    
    LANGUAGE_CHOICES = [
        ('Amharic', 'Amharic'),
        ('Oromigna', 'Oromigna'),
        ('Tigrigna', 'Tigrigna'),
        ('Somaligna', 'Somaligna'),
        ('Sidamigna', 'Sidamigna'),
    ]

    # Bio Section
    first_name = forms.CharField(max_length=50, label="First Name")
    last_name = forms.CharField(max_length=50, label="Last Name")
    age = forms.IntegerField(label="Age")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label="Gender")
    address = forms.CharField(max_length=200, label="Address", required=False)

    # Identity Section
    government_id = forms.FileField(label="Upload Government ID", required=True)
    picture = forms.FileField(label="Upload Picture (optional)", required=False)

    # Profile Section
    job_type = forms.MultipleChoiceField(choices=JOB_TYPE_CHOICES, widget=forms.CheckboxSelectMultiple, label="Job Type", required=True)
    other_job = forms.CharField(max_length=50, label="Other Job", required=False)

    schedule = forms.ChoiceField(choices=SCHEDULE_CHOICES, widget=forms.RadioSelect, label="Work Schedule", required=True)

    languages = forms.MultipleChoiceField(choices=LANGUAGE_CHOICES, widget=forms.CheckboxSelectMultiple, label="Language Requirements", required=False)
    other_language = forms.CharField(max_length=50, label="Other Language", required=False)
    special_requirements = forms.CharField(max_length=300, widget=forms.Textarea, label="Special Requirements", required=False)

    salary = forms.DecimalField(max_digits=10, decimal_places=2, label="Monthly Salary Budget", required=False)

    # Agreement Section
    agreement_signature = forms.CharField(max_length=100, label="Agreement Signature", required=True)