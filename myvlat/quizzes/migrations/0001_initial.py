# Generated by Django 3.2 on 2022-05-03 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('choice_id', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='choice_id')),
                ('user_id', models.CharField(max_length=256, verbose_name='사용자')),
                ('quiz_id', models.SmallIntegerField(verbose_name='quiz_id')),
                ('choice', models.CharField(max_length=64, verbose_name='답안')),
                ('status', models.BooleanField(verbose_name='정답여부')),
            ],
            options={
                'verbose_name': '정답',
                'verbose_name_plural': '정답',
                'db_table': 'VLAT_Answer',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('set_id', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='set_id')),
                ('set_quiz', models.CharField(max_length=256, verbose_name='문제집합')),
            ],
            options={
                'verbose_name': '문제세트',
                'verbose_name_plural': '문제세트',
                'db_table': 'Set_Quiz',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='사용자')),
                ('statedate', models.CharField(max_length=256, verbose_name='응시일자')),
                ('user_age', models.CharField(max_length=256, null=True, verbose_name='연령대')),
                ('user_education', models.CharField(default='', max_length=256, null=True, verbose_name='최종학력')),
                ('user_major', models.CharField(max_length=256, null=True, verbose_name='전공')),
                ('purpose', models.CharField(max_length=256, null=True, verbose_name='목적')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='result_id')),
                ('correct_number', models.SmallIntegerField(verbose_name='정답개수')),
                ('time', models.CharField(max_length=64, verbose_name='소요시간')),
                ('set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.set', verbose_name='set_id')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.user', verbose_name='user_id')),
            ],
            options={
                'verbose_name': '결과',
                'verbose_name_plural': '결과',
                'db_table': 'VLAT_Result',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='quiz_id')),
                ('v_number', models.SmallIntegerField(verbose_name='문제번호')),
                ('v_title', models.TextField(verbose_name='시각화제목')),
                ('v_type', models.CharField(max_length=256, verbose_name='시각화종류')),
                ('title', models.CharField(max_length=256, verbose_name='문제제목')),
                ('examples_1', models.CharField(max_length=64, verbose_name='보기1')),
                ('examples_2', models.CharField(max_length=64, verbose_name='보기2')),
                ('examples_3', models.CharField(blank=True, max_length=64, null=True, verbose_name='보기3')),
                ('examples_4', models.CharField(blank=True, max_length=64, null=True, verbose_name='보기4')),
                ('correct', models.CharField(max_length=64, verbose_name='정답')),
                ('set_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.set', verbose_name='set_id')),
            ],
            options={
                'verbose_name': '퀴즈',
                'verbose_name_plural': '퀴즈',
                'db_table': 'Vlat_Quiz',
            },
        ),
    ]
