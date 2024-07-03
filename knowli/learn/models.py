from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from account.models import Profile

# Create your models here.
class MathTest(models.Model):
    EGZAMIN8 = 'egzamin8'
    MATURA = 'matura'
    
    LEVEL_CHOICES = [
        (EGZAMIN8, 'Egzamin ósmoklasisty'),
        (MATURA, 'Matura'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    level = models.CharField(
        max_length=100,
        choices=LEVEL_CHOICES,
        default=EGZAMIN8,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MathTest, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('take_test', kwargs={'slug': self.slug})

class MathTask(models.Model):
    test = models.ForeignKey(MathTest, on_delete=models.CASCADE)
    question = models.TextField()
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100, blank=True, null=True)
    choice4 = models.CharField(max_length=100, blank=True, null=True)
    correct_choice = models.CharField(max_length=100, choices=(
        ('choice1', 'Choice 1'),
        ('choice2', 'Choice 2'),
        ('choice3', 'Choice 3'),
        ('choice4', 'Choice 4'),
    ))

    def __str__(self):
        return f"Task {self.id} of {self.test}"
    
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(MathTest, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.test.title}: {self.score}"