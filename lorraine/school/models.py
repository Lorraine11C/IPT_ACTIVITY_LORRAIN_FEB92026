from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    subject_specialty = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')

    def __str__(self):
        return f"{self.code} - {self.title}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True, editable=False)
    email      = models.EmailField(unique=True, blank=True, null=True)
    courses    = models.ManyToManyField(Course, related_name='students', blank=True)

    def save(self, *args, **kwargs):
        if not self.student_id:
            # Get the highest existing number and add 1
            last_student = Student.objects.order_by('-id').first()
            if last_student and last_student.student_id.isdigit():
                next_num = int(last_student.student_id) + 1
            else:
                next_num = 1
            self.student_id = str(next_num)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"
        
