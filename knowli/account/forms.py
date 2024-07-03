from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from account.models import Profile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput)
    education_level = forms.ChoiceField(choices=Profile.EDUCATION_CHOICES, label='Stopień nauki', widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']      
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            validate_password(password, self.instance)
        return password
    
    def clean_password2(self):
        cd = self.cleaned_data
        password = cd.get('password')
        password2 = cd.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('Hasła nie są takie same.')
        return password2
    
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        
        if qs.exists():
            raise forms.ValidationError('Ten e-mail jest zajęty.')
        return data
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        
