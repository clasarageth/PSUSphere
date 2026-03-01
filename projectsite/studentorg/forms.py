from django.forms import ModelForm
from django import forms
from .models import Organization
class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

from .models import OrgMember
class OrgMemberForm(ModelForm):
    class Meta:
        model = OrgMember
        fields = "__all__"

from .models import Student
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

from .models import College
class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"

from .models import Program
class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = "__all__"