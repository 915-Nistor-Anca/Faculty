from django.db import models

# Create your models here.

class Animal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    specie = models.CharField(max_length=100, blank=True, default='')
    birth_date = models.DateField()
    kilograms = models.IntegerField()
    gender = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name + ";" + self.specie + ";" + str(self.birth_date) + ";" + str(self.kilograms) + ";" + self.gender + "."

    class Meta:
        ordering = ['created']
