
from django.contrib import admin
from django.urls import path,include

# from my_app.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("my_app.urls") ),
]
