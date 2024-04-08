from django.core.validators import RegexValidator
from django.db import models


class Project(models.Model):
    nomi = models.CharField(max_length=150)
    malumot = models.TextField(max_length=555)
    rasm = models.ImageField(upload_to='project_images/')
    url = models.URLField()
    github_url = models.URLField()

    def __str__(self):
        return self.nomi


class Contact(models.Model):
    ism_familiya = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=128, validators=[
        RegexValidator(
            regex=r'^\+?998?\d{9,13}$',
            message="Phone number must be entered in the format: '+123456789'. Up to 15 digits"
        )])
    xabar = models.TextField(max_length=1000)

    def __str__(self):
        return self.ism_familiya
