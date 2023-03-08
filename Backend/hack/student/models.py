from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trophies = models.IntegerField(default=1000, blank=True, null=True)

    def __str__(self):
          return self.user.username

def validate_file_extension(value):
	if value.file.content_type != 'application/pdf':
		raise ValidationError(' only pdf allowed')

def file_size(value):
	limit = 512
	if value.size > limit:
		raise ValidationError('File too large. Size should not exceed 512KB.')

class notes(models.Model):
    host =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    file = models.FileField()
    description = models.TextField(null=True, blank=True)
    stds = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    std = models.CharField(max_length=2, choices=stds, default='1')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        # return str(self.name)
        return self.name

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

class JoinUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True,unique=True)
    description = models.TextField()

    def __str__(self):
         return self.email 
# Create your models here.
	
