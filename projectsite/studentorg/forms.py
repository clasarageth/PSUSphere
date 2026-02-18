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