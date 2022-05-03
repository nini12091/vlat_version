from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count

class User(models.Model):
    user_id = models.CharField(primary_key=True, verbose_name='사용자', max_length=256)
    statedate = models.CharField(verbose_name='응시일자', max_length=256)
    user_age = models.CharField(verbose_name='연령대', max_length=256, null=True)
    user_education = models.CharField(verbose_name='최종학력', max_length=256, null=True)
    user_major = models.CharField(verbose_name='전공', max_length=256, null=True)
    purpose = models.CharField(verbose_name='목적', max_length=256, null=True)

    def __str__(self):
        return str(self.statedate) + ' - ' + str(self.user_id)
    
    class Meta:
        db_table = 'User'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
    

class Quiz(models.Model):
    quiz_id = models.SmallIntegerField(verbose_name='quiz_id', primary_key=True)
    set_id = models.ForeignKey(
        'Set', on_delete=models.CASCADE, verbose_name='set_id')
    v_number = models.SmallIntegerField(verbose_name='문제번호')
    v_title = models.TextField(verbose_name='시각화제목')
    v_type = models.CharField(max_length=256, verbose_name='시각화종류')
    title = models.CharField(max_length=256, verbose_name='문제제목')
    examples_1 = models.CharField(max_length=64, verbose_name='보기1')
    examples_2 = models.CharField(max_length=64, verbose_name='보기2')
    examples_3 = models.CharField(
        max_length=64, null=True, blank=True, verbose_name='보기3')
    examples_4 = models.CharField(
        max_length=64, null=True, blank=True, verbose_name='보기4')
    correct = models.CharField(max_length=64, verbose_name='정답')

    def __str__(self):
        return str(self.set_id) + ' - ' + str(self.quiz_id) + ' - ' + str(self.v_type) + ' / ' + str(self.title)

    class Meta:
        db_table = 'Vlat_Quiz'
        verbose_name = '퀴즈'
        verbose_name_plural = '퀴즈'


class Set(models.Model):
    set_id = models.SmallIntegerField(verbose_name='set_id', primary_key=True)
    set_quiz = models.CharField(max_length=256, verbose_name='문제집합')

    def __str__(self):
        return str(self.set_id)

    class Meta:
        db_table = 'Set_Quiz'
        verbose_name = '문제세트'
        verbose_name_plural = '문제세트'

class Answer(models.Model):
    choice_id = models.CharField(verbose_name='choice_id', primary_key=True, max_length=256)
    user_id = models.CharField(verbose_name='사용자', max_length=256)
    quiz_id = models.SmallIntegerField(verbose_name='quiz_id')
    choice = models.CharField(max_length=64, verbose_name='답안')
    status = models.BooleanField(verbose_name='정답여부')

    def __str__(self):
        return str(self.user_id) + ' - '+ str(self.quiz_id) + ' - ' + str(self.choice) + '/' + str(self.status)

    class Meta:
        db_table = 'VLAT_Answer'
        verbose_name = '정답'
        verbose_name_plural = '정답'

class Result(models.Model):
    result_id = models.CharField(verbose_name='result_id', primary_key=True, max_length=256)      
    set_id = models.ForeignKey(
        'Set', on_delete=models.CASCADE, verbose_name='set_id')
    user_id = models.ForeignKey(
        'User', on_delete=models.CASCADE, verbose_name='user_id')
    correct_number = models.SmallIntegerField(verbose_name='정답개수')
    time = models.CharField(max_length=64, verbose_name='소요시간')

    def __str__(self):
        return str(self.set_id) + ' - ' + str(self.user_id) + ' - ' + str(self.correct_number)

    class Meta:
        db_table = 'VLAT_Result'
        verbose_name = '결과'
        verbose_name_plural = '결과'
        