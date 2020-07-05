from django import forms
from django.forms import ModelForm
from offsprings.models import Offspring


class CreateOffspringForm(ModelForm):

    class Meta:
        BIRTH_YEAR_CHOICES = ['2012,','2013', '2012', '2014', '2015',]
        model = Offspring
        fields = ['first_name', 'birth_date', 'grade',
                  'home_address', 'school', 'baptized', ]
        widgets = {
            'birth_date': forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
        }

    def clean_grade(self):
        grade = self.cleaned_data['grade']
        if grade != 1:
            raise forms.ValidationError(
                'Sólo se puede dar de alta a alumnos de primero de primaria, contacte con la parroquia para dar de alta a alumnos de otros cursos', code='wrong_grade')
        return grade
