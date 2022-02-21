# Generated by Django 3.2 on 2022-02-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_auto_20211108_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='purpose',
            field=models.CharField(max_length=256, null=True, verbose_name='목적'),
        ),
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
        migrations.AlterField(
            model_name='user',
            name='user_major',
            field=models.CharField(max_length=256, null=True, verbose_name='전공'),
        ),
    ]