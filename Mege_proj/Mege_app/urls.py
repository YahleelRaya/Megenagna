from django.urls import path

from . import views

urlpatterns = [
     path('retrieve/<str:user_type>/', views.retrieve, name='retrieve'),
     path("submit/",views.submit,name="submit"),
     path('add/',views.add_user),
     path('find/',views.get_all_users),
]
    # path("Employer_Registration/", views.retrieve, name="Yahleel"),
    
