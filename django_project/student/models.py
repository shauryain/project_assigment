from django.db import models

# Create your models here.

class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()


    class Meta:
        db_table ="students"

    def __str__(self):
        return f'student:{self.first_name}:{self.last_name}'

