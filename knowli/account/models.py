from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    EDUCATION_CHOICES = [
        ('primary', 'Szkoła podstawowa'),
        ('secondary', 'Szkoła średnia'),
    ]
    
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    education_level = models.CharField(max_length=20, choices=EDUCATION_CHOICES, default='primary')
    
    def __str__(self):
        return f'Profil użytkownika {self.user.username}'