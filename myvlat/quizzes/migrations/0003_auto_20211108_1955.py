# Generated by Django 3.2 on 2021-11-08 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_auto_20211025_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_age',
            field=models.CharField(max_length=256, null=True, verbose_name='연령대'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_education',
            field=models.CharField(max_length=256, null=True, verbose_name='최종학력'),
        ),
    ]