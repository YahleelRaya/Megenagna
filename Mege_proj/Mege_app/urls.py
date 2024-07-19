from django.urls import path

from . import views

urlpatterns = [
     path("Employer_Registration/", views.retrieve, name="Yahleel"),
     path("submit/",views.submit,name="submit")
]