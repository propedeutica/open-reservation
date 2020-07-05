#
# Overriding forms from allauth to use Patternfly
#

from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django.contrib.auth import get_user_model
from django import forms
from allauth.account.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList


class BootstrapErrorList(ErrorList):
    def as_divs(self):
        if not self:
            return ''
        return '%s' % ''.join(['<div class="alert alert-danger">%s</div>' % e for e in self])

    def __str__(self):
        return self.as_divs()


class MyCustomLoginForm(LoginForm):
    def login(self, *args, **kwargs):

        return super(MyCustomLoginForm, self).login(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update(
            {'class': 'form-control  input-lg'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control  input-lg'})


class MyCustomSignupForm(UserCreationForm):
    error_css_class = 'has-error'

    class Meta:
        model = get_user_model()

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control input-lg'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'offsprings_surname': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'phone': PhoneNumberInternationalFallbackWidget(attrs={'class': 'form-control input-lg'}),
            'phone2': PhoneNumberInternationalFallbackWidget(attrs={'class': 'form-control input-lg'}),
            'phone3': PhoneNumberInternationalFallbackWidget(attrs={'class': 'form-control input-lg'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control input-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control input-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control input-lg'}),
            'comments': forms.TextInput(attrs={'class': 'form-control input-lg'}),

        }
        fields = ('email', 'first_name', 'last_name',
                  'phone', 'phone2', 'phone3',
                  'offsprings_surname', 'father_name', 'mother_name')

    def __init__(self, *args, **kwargs):
        new_kwargs = {'error_class': BootstrapErrorList}
        new_kwargs.update(kwargs)
        super().__init__(*args, **new_kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control  input-lg'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control  input-lg'}
        )
