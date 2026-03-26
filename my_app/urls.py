from django.urls import path
from my_app.views import *

urlpatterns = [
    path("", home_page, name="home_page"),
    path("student", student_data, name="student_model"),
    path("course", course_data, name="course_model"),
    path("enroll", enroll_data, name="enroll_model"),
]
