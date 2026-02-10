from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework import generics
from .models import Student, Course, Teacher
from .serializers import StudentSerializer, CourseSerializer, TeacherSerializer

# ── API Views (DRF) ────────────────────────────────────────
class StudentListCreateAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseListCreateAPI(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# ── Template Views (simple dashboard feel) ─────────────────
class DashboardView(View):
    def get(self, request):
        context = {
            'student_count': Student.objects.count(),
            'course_count': Course.objects.count(),
            'teacher_count': Teacher.objects.count(),
        }
        return render(request, 'school/dashboard.html', context)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'school/student_list.html', {'students': students})

def student_create_or_update(request, pk=None):
    if pk:
        student = get_object_or_404(Student, pk=pk)
    else:
        student = None

    if request.method == 'POST':
        data = request.POST
        if student:
            # Update existing
            student.first_name = data['first_name']
            student.last_name  = data['last_name']
            student.email      = data.get('email')
            student.save()
            student.courses.set(data.getlist('courses'))
        else:
            # Create new → student_id will be auto-generated in model.save()
            student = Student(
                first_name = data['first_name'],
                last_name  = data['last_name'],
                email      = data.get('email'),
            )
            student.save()                     # ← this triggers auto student_id
            student.courses.set(data.getlist('courses'))

        return redirect('student_list')

    courses = Course.objects.all()
    return render(request, 'school/student_form.html', {
        'student': student,
        'courses': courses
    })

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'school/student_confirm_delete.html', {'student': student})

# You can add similar views for Course & Teacher if you want


def course_list(request):
    courses = Course.objects.all().select_related('teacher')
    return render(request, 'school/course_list.html', {'courses': courses})

def course_create_or_update(request, pk=None):
    if pk:
        course = get_object_or_404(Course, pk=pk)
    else:
        course = None

    if request.method == 'POST':
        data = request.POST
        teacher = None
        if data.get('teacher'):
            teacher = get_object_or_404(Teacher, pk=data['teacher'])

        if course:
            course.title = data['title']
            course.code = data['code']
            course.description = data.get('description', '')
            course.teacher = teacher
            course.save()
        else:
            Course.objects.create(
                title=data['title'],
                code=data['code'],
                description=data.get('description', ''),
                teacher=teacher
            )
        return redirect('course_list')

    # ── Key change: Filter teachers with no courses ────────────────────────
    # Teachers who have 0 courses (using related_name='courses')
    available_teachers = Teacher.objects.filter(courses__isnull=True)

    # If editing: also include the current teacher (even if they already have this course)
    if course and course.teacher:
        # We include the currently assigned teacher so user can keep or change
        available_teachers = available_teachers | Teacher.objects.filter(pk=course.teacher.pk)

    # Optional: remove duplicates (in case current teacher was already in the filter)
    available_teachers = available_teachers.distinct()

    return render(request, 'school/course_form.html', {
        'course': course,
        'teachers': available_teachers   # ← only pass filtered list
    })

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'school/course_confirm_delete.html', {'course': course})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teacher_list.html', {'teachers': teachers})

def teacher_create_or_update(request, pk=None):
    if pk:
        teacher = get_object_or_404(Teacher, pk=pk)
    else:
        teacher = None

    if request.method == 'POST':
        data = request.POST
        if teacher:
            teacher.name = data['name']
            teacher.email = data.get('email')
            teacher.subject_specialty = data.get('subject_specialty', '')
            teacher.save()
        else:
            Teacher.objects.create(
                name=data['name'],
                email=data.get('email'),
                subject_specialty=data.get('subject_specialty', '')
            )
        return redirect('teacher_list')

    return render(request, 'school/teacher_form.html', {
        'teacher': teacher
    })

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'school/teacher_confirm_delete.html', {'teacher': teacher})