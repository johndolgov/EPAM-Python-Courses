from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField('Artist name', max_length=100,
                            help_text='write artist name here')
    age = models.CharField('Age', max_length=1000, default=18)

    def __str__(self):
        return f'{self.name} with {self.age}'
