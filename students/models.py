from django.db import models
from faker import Faker


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'

    @staticmethod
    def gen_students(cnt=10):
        fk = Faker()
        for _ in range(cnt):
            st = Student(
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                age=fk.random_int(min=18, max=45)
            )

            st.save()
