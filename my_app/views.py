from django.shortcuts import render, redirect
from my_app.models import *


# Create your views here.
def home_page(request):

    return render(request, "home.html")


def student_data(request):
    if request.method == "POST":
        stu_name = request.POST.get("student_name")
        stu_email = request.POST.get("student_email")
        stu_phone = request.POST.get("student_phone")
        stu_address = request.POST.get("student_address")
        Student_Model.objects.create(
            name=stu_name, email=stu_email, phone=stu_phone, address=stu_address
        )
        return redirect("student_model")

    data = Student_Model.objects.all()
    single_data = Student_Model.objects.get(id=2)
    filter_data = Student_Model.objects.filter(name="Shelly")
    data_pack = {
        "title": "Student Information Table",
        "item": data,
        "single_item": single_data,
        "filter_item": filter_data,
    }
    return render(
        request,
        "student.html",
        data_pack,
    )


def student_details(request, stu_id):
    data = Student_Model.objects.get(id=stu_id)
    data_pack = {"item": data}
    return render(request, "student_details.html", data_pack)


def course_data(request):
    if request.method == "POST":
        c_title = request.POST.get("course_title")
        c_fee = request.POST.get("course_fee")
        c_duration = request.POST.get("course_duration")
        c_name = request.POST.get("instructor_name")

        Course_Model.objects.create(
            title=c_title, fee=c_fee, duration=c_duration, instructor_name=c_name
        )

    data = Course_Model.objects.all()
    single_data = Course_Model.objects.get(id=3)
    filter_data = Course_Model.objects.filter(fee__gt=3000)
    data_pack = {
        "title": "Course Directory",
        "item": data,
        "single_item": single_data,
        "filter_item": filter_data,
    }
    return render(request, "course.html", data_pack)


def course_details(request, c_id):
    data = Course_Model.objects.get(id=c_id)
    data_pack = {"item": data}
    return render(request, "course_details.html", data_pack)


def enroll_data(request):
    if request.method == "POST":
        e_name = request.POST.get("student_name")
        e_title = request.POST.get("course_title")
        e_status = request.POST.get("status")

        Enrollment_Model.objects.create(
            student_name=e_name, course_title=e_title, status=e_status
        )

    data = Enrollment_Model.objects.all()
    filter_data = Enrollment_Model.objects.filter(status="Enrolled")
    data_pack = {
        "title": "Enrollment Directory",
        "item": data,
        "filter_item": filter_data,
    }
    return render(request, "enrollment.html", data_pack)

def enroll_details(request):
    return render(request)
