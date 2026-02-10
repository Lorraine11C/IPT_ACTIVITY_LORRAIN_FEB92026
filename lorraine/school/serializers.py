from rest_framework import serializers
from .models import Teacher, Course, Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'subject_specialty']

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True, required=False
    )

    class Meta:
        model = Course
        fields = ['id', 'title', 'code', 'description', 'teacher', 'teacher_id']

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    course_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), many=True, source='courses', write_only=True, required=False
    )

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'student_id', 'email', 'courses', 'course_ids']