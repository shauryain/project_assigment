from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("<int:id>",views.view_student,name="view_student") #path convert that allows  create daynamin url int matches integer  when djanog  is pregenting with urls mathcing this pattern for example /5 django puts integer 5 into the variable(give id 5 your id is matche id gives us id 5 relted think)
]
