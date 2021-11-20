from django.test import TestCase
from ..models import *
from datetime import datetime


class TestStudentModel(TestCase):
    def test_student_str(self):
        birth = datetime.now()
        firstname = Student.objects.create(firstname="test")
        lastname = Student.objects.create(lastname="test")
        #birth_day = Student.objects.create(bithdate=birth)
        email = Student.objects.create(email="test@testing.com")
        state = Student.objects.create(state=Student.Std_state[0])

        self.assertEqual(str(firstname), "test")

