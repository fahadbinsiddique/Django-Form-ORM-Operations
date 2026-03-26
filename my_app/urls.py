from django.urls import path
from my_app.views import *

urlpatterns = [
    path("", home_page, name="home_page"),
    path("student", student_data, name="student_model"),
    path("course", course_data, name="course_model"),
    path("enroll", enroll_data, name="enroll_model"),
    path("student-details/<str:stu_id>/", student_details, name="student_details"),
    path("course-details/<str:c_id>/", course_details, name="course_details"),
    path("enroll-details/<str:e_id>/", enroll_details, name="enroll_details"),
]
