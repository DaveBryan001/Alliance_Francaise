from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dal import autocomplete
from django import forms
from .models import Course


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    class CourseForm(forms.ModelForm):
        class Meta:
            model = Course
            fields = ['name']
            widgets = {
                'name': autocomplete.ModelSelect2(url='course-autocomplete')
            }