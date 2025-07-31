from django.urls import path
from . import views
from .views import create_course_view
from .views import enroll_course_view

app_name = 'courses'
urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('add/', views.add_course, name='add_course'),
    path('create/', views.create_course_view, name='create_course'),
    path('enrolled/', views.enrolled_courses_view, name='enrolled_courses'),
    path('all/', views.all_courses_view, name='all_courses'),
    path('<int:course_id>/enroll/', enroll_course_view, name='enroll_course'),
    path('enroll/<int:course_id>/', views.enroll_view, name='enroll'),
    path('enroll/<int:course_id>/', views.enroll_course_view, name='enroll_course'),
    path('unenroll/<int:course_id>/', views.unenroll_course_view, name='unenroll_course')

]
