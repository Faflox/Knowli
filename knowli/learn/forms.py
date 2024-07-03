from django import forms
from learn.models import MathTask

class MathTaskForm(forms.ModelForm):
    class Meta:
        model = MathTask
        fields = ['choice1', 'choice2', 'choice3', 'choice4']

