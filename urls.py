from django.urls import path
from . import views

urlpatterns = [
    path("",views.start ),
    path("again_start",views.start,name="again_start"),
    path("register",views.register,name="register" ),
    path("saving",views.saving , name="saving"),
    path("attendence_form",views.attendence_form , name="attendence_from"),
    path("attendence",views.attendence , name="attendence"),
]


