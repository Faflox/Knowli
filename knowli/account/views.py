from django.shortcuts import render
from account.forms import UserRegistrationForm
from account.models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            
            Profile.objects.create(user=new_user, education_level=user_form.cleaned_data['education_level'])
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 
                  'registration/register.html',
                  {'user_form': user_form})