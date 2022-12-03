from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('studentinfo/<int:pk>',views.student_detail,name="studentinfo"),
    path('studentlist/',views.student_list,name="studentlist"),
]
