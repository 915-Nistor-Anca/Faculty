from django.db import models

# Create your models here.
class Area(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=10, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    allocated_budget = models.IntegerField()
    needs_rebuilding = models.BinaryField()


class Specie(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100, blank=True, default='')
    specifications = models.CharField(max_length=100, blank=True, default='')
    endangered = models.BinaryField()
    years_expected_to_live = models.IntegerField()
    food_type = models.CharField(max_length=100, blank=True, default='')

    area = models.ForeignKey(Area, on_delete=models.CASCADE)



class Animal(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100, blank=True, default='')
    birth_date = models.DateField()
    kilograms = models.IntegerField()
    gender = models.CharField(max_length=100, blank=True, default='')
    favourite_toy = models.CharField(max_length=100, blank=True, default='')

    specie = models.ForeignKey(Specie, on_delete=models.CASCADE, related_name='content')
    content = models.TextField(default='default_value')



    class Meta:
        ordering = ['created']
