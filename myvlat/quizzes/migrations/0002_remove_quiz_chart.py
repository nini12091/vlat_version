# Generated by Django 3.2 on 2021-06-22 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='chart',
        ),
    ]
