# Generated by Django 4.1.7 on 2023-03-19 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0012_remove_specie_species'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='content',
        ),
    ]