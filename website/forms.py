from django import forms
from .models import Project, Inquiry, Testimony, TechStack


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            'project_name',
            'description',
            'tech_stacks',
            'link'
        ]

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 5
                }
            ),
            'tech_stacks': forms.CheckboxSelectMultiple()
        }


class TechStackForm(forms.ModelForm):

    class Meta:
        model = TechStack

        fields = [
            'name'
        ]
class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry

        fields = [
            'first_name',
            'last_name',
            'contact_number',
            'email',
            'address',
            'message'
        ]


class TestimonyForm(forms.ModelForm):

    class Meta:
        model = Testimony

        fields = [
            'full_name',
            'content'
        ]