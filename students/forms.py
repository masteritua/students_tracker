from django.forms import forms, ModelForm
from students.models import Student

class StudentsAddForm(ModelForm):
    pass
    class Meta:
        model = Student
        fields = "__all__"