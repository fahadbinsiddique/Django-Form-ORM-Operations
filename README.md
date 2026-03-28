# 🎓 Django Form & ORM Operations

A beginner-friendly Django web application demonstrating **HTML Form handling** and **Django ORM operations** through a simple Course Management System.

> 🌐 **Live Demo:** [django-form-orm-operations.onrender.com](https://django-form-orm-operations.onrender.com) <br/>
> 📁 **Repository:** [fahadbinsiddique/Django-Form-ORM-Operations](https://github.com/fahadbinsiddique/Django-Form-ORM-Operations)

---

## 📌 About The Project

This project was built to practice core Django concepts — specifically how to take user input through HTML forms and store/retrieve data using Django's powerful ORM (Object Relational Mapper). It manages three entities: **Students**, **Courses**, and **Enrollments**.

---

## ✨ Features

- ➕ Add new Students, Courses, and Enrollments via HTML forms
- 📋 View all records in a clean table layout
- 🔍 View individual record details
- 🔎 Filter data using ORM queries
- 🛠️ Django Admin Panel support
- 🎨 Responsive UI with Template Inheritance

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python 3.14 | Backend language |
| Django 6.x | Web framework |
| SQLite | Database |
| HTML & CSS | Frontend |
| Render | Deployment platform |

---

## 📂 Project Structure

```
my_project/
├── my_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── masters/
│   │   │   ├── base.html
│   │   │   └── nav.html
│   │   ├── home.html
│   │   ├── student.html
│   │   ├── student_details.html
│   │   ├── course.html
│   │   ├── course_details.html
│   │   ├── enrollment.html
│   │   └── enroll_details.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── my_project/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── Procfile
└── runtime.txt
```

---

## 🗄️ Models

### Student_Model
| Field | Type |
|---|---|
| name | CharField |
| email | CharField |
| phone | CharField |
| address | TextField |

### Course_Model
| Field | Type |
|---|---|
| title | CharField |
| fee | IntegerField |
| duration | IntegerField |
| instructor_name | CharField |

### Enrollment_Model
| Field | Type |
|---|---|
| student_name | CharField |
| course_title | CharField |
| status | CharField |

---

## ⚙️ ORM Queries Used

```python
# Create a new record
Student_Model.objects.create(name=..., email=..., phone=..., address=...)

# Get all records
Student_Model.objects.all()

# Get a single record by ID
Student_Model.objects.get(id=1)

# Filter records by condition
Student_Model.objects.filter(name="John")
Course_Model.objects.filter(fee__gt=3000)  # fee greater than 3000
Enrollment_Model.objects.filter(status="Not Enrolled")
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- pip installed

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/fahadbinsiddique/Django-Form-ORM-Operations.git

# 2. Navigate to project folder
cd Django-Form-ORM-Operations/my_project

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

Then open your browser and go to: `http://127.0.0.1:8000`

---

## 🔗 URL Routes

| URL | Description |
|---|---|
| `/` | Home Page |
| `/student` | Student list & add form |
| `/course` | Course list & add form |
| `/enroll` | Enrollment list & add form |
| `/student-details/<id>/` | Single student details |
| `/course-details/<id>/` | Single course details |
| `/enroll-details/<id>/` | Single enrollment details |



---

## 🧠 What I Learned

- How Django ORM works under the hood
- Handling GET and POST requests in views
- Template inheritance to avoid code repetition
- Deploying a Django project on Render

---

## 🙋‍♂️ Author

**Fahad Bin Siddique**
- GitHub: [@fahadbinsiddique](https://github.com/fahadbinsiddique)
- LinkedIn: [@fahadbinsiddique](https://www.linkedin.com/in/fahadbinsiddique/)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
