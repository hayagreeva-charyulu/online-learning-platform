from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import CourseForm
from .models import Enrollment
from django.contrib import messages

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def add_course(request):
    if request.user.role != 'creator':
        return redirect('course_list')
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})

def create_course_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.creator = request.user
            course.save()
            return redirect('dashboard')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Prevent duplicate enrollments
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)

    if created:
        messages.success(request, f"You have enrolled in {course.title}")
    else:
        messages.info(request, f"You are already enrolled in {course.title}")

    return redirect('course_detail', course_id=course.id)

def enrolled_courses_view(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'courses/enrolled_courses.html', {'enrollments': enrollments})

def dashboard_view(request):
    if request.user.role == 'creator':
        courses = Course.objects.filter(created_by=request.user)
    else:
        courses = request.user.courses_enrolled.all()
    return render(request, 'main/dashboard.html', {'courses': courses})

@login_required
def course_list(request):
    user = request.user
    enrolled_courses = user.enrolled_courses.all()  # Related name from your Course model
    available_courses = Course.objects.exclude(id__in=enrolled_courses.values_list('id', flat=True))

    return render(request, 'courses/course_list.html', {
        'courses': available_courses,
    })


def all_courses_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/all_courses.html', {'courses': courses})




