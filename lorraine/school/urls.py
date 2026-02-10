from django.urls import path
from . import views

urlpatterns = [
    # Template views
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create_or_update, name='student_add'),
    path('students/<int:pk>/edit/', views.student_create_or_update, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # DRF API endpoints
    path('api/students/', views.StudentListCreateAPI.as_view(), name='api-student-list'),
    path('api/students/<int:pk>/', views.StudentDetailAPI.as_view(), name='api-student-detail'),
    path('api/courses/', views.CourseListCreateAPI.as_view(), name='api-course-list'),
    path('api/courses/<int:pk>/', views.CourseDetailAPI.as_view(), name='api-course-detail'),

    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_create_or_update, name='course_add'),
    path('courses/<int:pk>/edit/', views.course_create_or_update, name='course_edit'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),

    # Teachers
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.teacher_create_or_update, name='teacher_add'),
    path('teachers/<int:pk>/edit/', views.teacher_create_or_update, name='teacher_edit'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
]