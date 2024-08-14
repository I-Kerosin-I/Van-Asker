from django import forms
from qstn.models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('login', 'password', 'email', 'first_name', 'last_name', 'patronymic', 'birth',
                  'educational_institution')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-field'}),
            'password': forms.PasswordInput(attrs={'class': 'form-field'}),
            'email': forms.EmailInput(attrs={'class': 'form-field'}),
            'first_name': forms.TextInput(attrs={'class': 'form-field'}),
            'last_name': forms.TextInput(attrs={'class': 'form-field'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-field'}),
            'birth': forms.DateInput(attrs={'class': 'form-field', 'type': 'date'}),
            'educational_institution': forms.TextInput(attrs={'class': 'form-field'}),
        }
        labels = {
            'username': 'Логин',
            'password': 'Пароль',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'patronymic': 'Отчество',
            'birth': 'Дата рождения',
            'educational_institution': 'Образовательное учреждение'
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
