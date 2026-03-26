from django.shortcuts import render, redirect
from my_app.models import *


# Create your views here.
def home_page(request):
    if request.method == "POST":
        stu_name = request.POST.get("student_name")
        stu_email = request.POST.get("student_email")
        stu_phone = request.POST.get("student_phone")
        stu_address = request.POST.get("student_address")

        Student_Model.objects.create(
            name=stu_name, email=stu_email, phone=stu_phone, address=stu_address
        )
        return redirect("student_model")
    return render(request, "home.html")


def student_data(request):
    data = Student_Model.objects.all()
    single_data = Student_Model.objects.get(id=2)
    filter_data = Student_Model.objects.filter(name="Shelly Kerluke")
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


def course_data(request):
    data = Course_Model.objects.all()
    data_pack = {"title": "Course Directory", "item": data}
    return render(request, "course.html", data_pack)


def enroll_data(request):
    data = Enrollment_Model.objects.all()
    data_pack = {"title": "Enrollment Directory", "item": data}
    return render(request, "enrollment.html", data_pack)
