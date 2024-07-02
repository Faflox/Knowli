from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)
    date_taken = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.test_name}"