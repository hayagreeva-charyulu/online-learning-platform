
# Create your views here.
from django.shortcuts import render
from courses.models import Course

def dashboard_view(request):
    user = request.user
    if user.profile.role == 'teacher':
        courses = user.courses_taught.all()
    else:
        courses = user.courses_enrolled.all()

    return render(request, 'main/dashboard.html', {'courses': courses})

