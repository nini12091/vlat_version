from telnetlib import STATUS
from urllib import response
from django.http import HttpResponseRedirect, HttpResponse
from .models import Quiz, User, Answer
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
import csv
from django.db.models import Q

def index(request):
    # Session 생성
    request.session.create()
    userID = str(request.session.session_key)
    today = str(timezone.now().strftime("%I:%M%p on %B %d, %Y"))
    request.session['userID'] = userID
    request.session['statedate'] = today

    return render(request, "index.html")

def quiz(request, quiz_id):
    if quiz_id <= 5:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz.html", context)

    elif 5 < quiz_id <= 9:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')
 
            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz2.html", context)

    elif 9 < quiz_id <= 14:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz3.html", context)
    
    elif 14 < quiz_id <= 17:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz4.html", context)
    
    elif 17 < quiz_id <= 20:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')
 
            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz5.html", context)

    elif 20 < quiz_id <= 23:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')
  
            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz6.html", context)

    elif 23 < quiz_id <= 30:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz7.html", context)

    elif 30 < quiz_id <= 34:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')
 
            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz8.html", context)

    elif 34 < quiz_id <= 40:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz9.html", context)

    elif 40 < quiz_id <= 47:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz10.html", context)

    elif 47 < quiz_id <= 50:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz11.html", context)

    elif 50 < quiz_id <= 54:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')
  
            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            if quiz_id == 54:
                return redirect('user')
            else:
                return HttpResponseRedirect(reverse('quiz', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz/quiz12.html", context)
    else:
        return render(request, "user.html")

def index2(request):
    # Session 생성
    request.session.create()
    userID = str(request.session.session_key)
    today = str(timezone.now().strftime("%I:%M%p on %B %d, %Y"))
    request.session['userID'] = userID
    request.session['statedate'] = today

    return render(request, "index2.html")

def quiz2(request, quiz_id):
    if quiz_id <= 105:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_1.html", context)

    elif 105 < quiz_id <= 109:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')
 
            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_2.html", context)

    elif 109 < quiz_id <= 114:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_3.html", context)
    
    elif 114 < quiz_id <= 117:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_4.html", context)
    
    elif 117 < quiz_id <= 120:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')
 
            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_5.html", context)

    elif 120 < quiz_id <= 123:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')
  
            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_6.html", context)

    elif 123 < quiz_id <= 130:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_7.html", context)

    elif 130 < quiz_id <= 134:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')
 
            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_8.html", context)

    elif 134 < quiz_id <= 140:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_9.html", context)

    elif 140 < quiz_id <= 147:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_10.html", context)

    elif 147 < quiz_id <= 150:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')

            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_11.html", context)

    elif 150 < quiz_id <= 154:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session['userID'])
            answer.user_id = request.session['userID']
            answer.quiz_id = request.session['quizId']
            answer.choice = request.POST.get('answer','')
  
            if answer.choice == quiz.correct:
                answer.status = True
            else:
                answer.status = False
            answer.save()
            if quiz_id == 154:
                return redirect('user')
            else:
                return HttpResponseRedirect(reverse('quiz2', args=(quiz_id,)))

        else:    
            request.session['quizId'] = quiz_id
            next_quiz_id = quiz_id + 1
            quiz_detail = get_object_or_404(Quiz, pk=quiz_id)
            context = {'quiz_detail':quiz_detail, 'next_quiz_id':next_quiz_id}
            return render(request, "quiz2/quiz2_12.html", context)
    else:
        return render(request, "user.html")

def user(request):
    if request.method == "POST":

        user_age = request.POST.get('user-age','')
        user_education = request.POST.get('user-education','')
        
        request.session['user_age'] = user_age
        request.session['user_education'] = user_education

        if user_education == "초등학교 재학" or user_education == "초등학교 졸업" or user_education == "중학교 졸업" or user_education == "고등학교 졸업":
            return redirect('user_end1')
        else:
            return redirect('user_end2')
    else:
        return render(request, "user.html")

def user_end1(request):
    if request.method == "POST":

        purpose = request.POST.get('purpose','')
        
        # Session DB 저장
        user = User()
        user.user_id = request.session['userID']
        user.statedate = request.session['statedate']
        user.user_age = request.session['user_age']
        user.user_education = request.session['user_education']
        user.purpose = purpose
        user.save()

        return redirect('quiz_result')
    else:
        return render(request, "user_end1.html")

def user_end2(request):
    if request.method == "POST":
        user_major = request.POST.get('user-major','')
        purpose = request.POST.get('purpose','')

        # Session DB 저장
        user = User()
        user.user_id = request.session['userID']
        user.statedate = request.session['statedate']
        user.user_age = request.session['user_age']
        user.user_education = request.session['user_education']
        user.user_major = user_major
        user.purpose = purpose
        user.save()

        return redirect('quiz_result')
    else:
        return render(request, "user_end2.html")

def quiz_result(request):
    userID = request.session['userID']
    answer = Answer.objects.filter(user_id = userID)
    correct_num= answer.filter(status=True).count()
    percent = (correct_num/53)*100
    quiz_id = []
    for v in answer:
        quiz_id.append(v.quiz_id)
    status = []
    for v in answer :
        status.append(str(v.status))

    context = {'userID':userID,'correct_num':correct_num, 'percent':percent, 'status':status,'quiz_id':quiz_id}
    return render(request, "quiz_result.html", context)

def result(request):
    if request.method == 'POST':
        user_id = request.POST.get('id-name')
        answer = Answer.objects.filter(user_id = user_id)
        correct_num= answer.filter(status=True).count()
        percent = (correct_num/53)*100
        quiz_id = []
        for v in answer:
            quiz_id.append(v.quiz_id)
        status = []
        for v in answer :
            status.append(str(v.status))
        context = {'user_id':user_id,'correct_num':correct_num, 'percent':percent, 'status':status,'quiz_id':quiz_id}
        return render(request, "result.html",context)

    return render(request, "result.html")

def about(request):
    return render(request, "about.html")

def exportcsv(request):
    resultdata = Answer.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=k_vlat_resultdata.csv'
    writer = csv.writer(response)
    writer.writerow(['choice_id', 'user_id', 'quiz_id', 'choice', 'status'])
    results = resultdata.values_list('choice_id', 'user_id', 'quiz_id', 'choice', 'status')
    for rlt in results:
        writer.writerow(rlt)
    return response

data = None
filedata =  './'

def read_data(table_name):
    with open(filedata + f'{table_name}.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        global data
        data = list(reader)
    return

def footer(table_name, class_name, bulk_list):
    class_name.objects.bulk_create(bulk_list)

    with open(filedata + f'{table_name}.csv','w') as csvfile:
        writer = csv.writer(csvfile)
    return

def add_data(request):
    read_data('k-vlat-0221')

    arr = []
    for row in data:
        if row[4] == "TRUE":
            row[4] = True
        else:
            row[4] = False
        arr.append(Answer(
            choice_id = row[0],
            user_id = row[1],
            quiz_id = row[2],
            choice = row[3],
            status = row[4]
        ))

    footer('k-vlat-0221', Answer, arr)
    return HttpResponse('Answers table updated')

def user_download(request):
    if request.method == 'POST':
        if request.POST.get("form-type") == 'form1':
            upload_file = request.FILES['upload-file']
            file = upload_file.read().decode('utf-8').splitlines()

            reader = csv.reader(file)

            global id_list
            
            id_list = []

            for id in reader:
                for data in id:
                    id_list.append(data)

            context = {'id_list':id_list}

            return render(request, "download.html", context)

        elif request.POST.get("form-type") == 'form2':

            option = request.POST.get('option-list','')
            
            if option == 'option1':

                list_user = []
                list_correct = []
                list_vis1 = []
                list_vis2 = []
                list_vis3 = []
                list_vis4 = []
                list_vis5 = []
                list_vis6 = []
                list_vis7 = []
                list_vis8 = []
                list_vis9 = []
                list_vis10 = []
                list_vis11 = []
                list_vis12 = []

                ## user_id별 결과 로우 데이터 추출
                for i in id_list:
                    correct = Answer.objects.filter(Q(user_id = i) & Q(status=True))
                    list_user.append(i)
                    list_correct.append(Answer.objects.filter(Q(user_id = i) & Q(status=True)).count())
                    list_vis1.append(correct.filter(Q(quiz_id=1)|Q(quiz_id=2)|Q(quiz_id=3)|Q(quiz_id=4)|Q(quiz_id=5)|Q(quiz_id=101)|Q(quiz_id=102)|Q(quiz_id=103)&Q(quiz_id=104)&Q(quiz_id=105)).count())
                    list_vis2.append(correct.filter(Q(quiz_id=6)|Q(quiz_id=7)|Q(quiz_id=8)|Q(quiz_id=9)|Q(quiz_id=106)|Q(quiz_id=107)|Q(quiz_id=108)|Q(quiz_id=109)).count())
                    list_vis3.append(correct.filter(Q(quiz_id=10)|Q(quiz_id=11)|Q(quiz_id=12)|Q(quiz_id=13)|Q(quiz_id=14)|Q(quiz_id=110)|Q(quiz_id=111)|Q(quiz_id=112)|Q(quiz_id=113)|Q(quiz_id=114)).count())
                    list_vis4.append(correct.filter(Q(quiz_id=15)|Q(quiz_id=16)|Q(quiz_id=17)|Q(quiz_id=115)|Q(quiz_id=116)|Q(quiz_id=117)).count())
                    list_vis5.append(correct.filter(Q(quiz_id=18)|Q(quiz_id=19)|Q(quiz_id=20)|Q(quiz_id=118)|Q(quiz_id=119)|Q(quiz_id=120)).count())
                    list_vis6.append(correct.filter(Q(quiz_id=21)|Q(quiz_id=22)|Q(quiz_id=23)|Q(quiz_id=121)|Q(quiz_id=122)|Q(quiz_id=123)).count())
                    list_vis7.append(correct.filter(Q(quiz_id=24)|Q(quiz_id=25)|Q(quiz_id=26)|Q(quiz_id=27)|Q(quiz_id=28)|Q(quiz_id=29)|Q(quiz_id=30)|Q(quiz_id=124)|Q(quiz_id=125)|Q(quiz_id=126)|Q(quiz_id=127)|Q(quiz_id=128)|Q(quiz_id=129)|Q(quiz_id=130)).count())
                    list_vis8.append(correct.filter(Q(quiz_id=31)|Q(quiz_id=32)|Q(quiz_id=33)|Q(quiz_id=34)|Q(quiz_id=131)|Q(quiz_id=132)|Q(quiz_id=133)|Q(quiz_id=134)).count())
                    list_vis9.append(correct.filter(Q(quiz_id=35)|Q(quiz_id=36)|Q(quiz_id=37)|Q(quiz_id=38)|Q(quiz_id=39)|Q(quiz_id=40)|Q(quiz_id=135)|Q(quiz_id=136)|Q(quiz_id=137)|Q(quiz_id=138)|Q(quiz_id=139)|Q(quiz_id=140)).count())
                    list_vis10.append(correct.filter(Q(quiz_id=41)|Q(quiz_id=42)|Q(quiz_id=43)|Q(quiz_id=44)|Q(quiz_id=45)|Q(quiz_id=46)|Q(quiz_id=47)|Q(quiz_id=141)|Q(quiz_id=142)|Q(quiz_id=143)|Q(quiz_id=144)|Q(quiz_id=145)|Q(quiz_id=146)|Q(quiz_id=147)).count())
                    list_vis11.append(correct.filter(Q(quiz_id=48)|Q(quiz_id=49)|Q(quiz_id=50)|Q(quiz_id=148)|Q(quiz_id=149)|Q(quiz_id=150)).count())
                    list_vis12.append(correct.filter(Q(quiz_id=51)|Q(quiz_id=52)|Q(quiz_id=53)|Q(quiz_id=151)|Q(quiz_id=152)|Q(quiz_id=153)).count())

                result_list1 = [['user_id','정답 수','Line_Chart(5)','Bar_Chart(4)','Stacked_Bar_Chart(5)','100%_Stacked_Bar_Chart(3)','Pie_Chart(3)','Histogram(3)','Scatter_Plot(7)','Area_Chart(4)','Stacked_Area_Chart(6)','Bubble_Chart(7)','Choropleth_Map(3)','Tree_Map(3)']]
                
                for l in range(len(list_user)):
                    arr = []
                    arr.append(list_user[l])
                    arr.append(list_correct[l])
                    arr.append(list_vis1[l])
                    arr.append(list_vis2[l])
                    arr.append(list_vis3[l])
                    arr.append(list_vis4[l])
                    arr.append(list_vis5[l])
                    arr.append(list_vis6[l])
                    arr.append(list_vis7[l])
                    arr.append(list_vis8[l])
                    arr.append(list_vis9[l])
                    arr.append(list_vis10[l])
                    arr.append(list_vis11[l])
                    arr.append(list_vis12[l])

                    result_list1.append(arr)

                response = HttpResponse('text/csv')
                response['Content-Disposition'] = 'attachment; filename=k_vlat_resultdata.csv'
                writer = csv.writer(response)
                
                for row in result_list1:
                    writer.writerow(row)

                return response
                

            if option == 'option2':
            
                list_user2 = []
                list_quiz_id = []
                list_vis_type = []
                list_vis_task = []
                list_status = []
                vis_type = ['Line_Chart','Bar_Chart','Stacked_Bar_Chart','100%_Stacked_Bar_Chart','Pie_Chart','Histogram','Scatter_Plot','Area_Chart','Stacked_Area_Chart','Bubble_Chart','Choropleth_Map','Tree_Map']
                vis_task = ['Retrieve_Values','Find_Extremum','Determine_Range','Characterize_Distribution','Find_Anomalies','Find_Clusters','Find_Correlation’Trens','Make_Comparison']

                for k in id_list:
                    user_list2 = Answer.objects.filter(user_id = k)
                    for ul in user_list2:
                        if ul.quiz_id == 1 or ul.quiz_id == 101 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[0])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 2 or ul.quiz_id == 102 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[0])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 3 or ul.quiz_id == 103 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[0])
                            list_vis_task.append(vis_task[2])
                            list_status.append(ul.status)
                        
                        elif ul.quiz_id == 4 or ul.quiz_id == 104 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[0])
                            list_vis_task.append(vis_task[6])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 5 or ul.quiz_id == 105 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[0])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 6 or ul.quiz_id == 106 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[1])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 7 or ul.quiz_id == 107 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[1])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 8 or ul.quiz_id == 108 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[1])
                            list_vis_task.append(vis_task[2])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 9 or ul.quiz_id == 109 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[1])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 10 or ul.quiz_id == 110 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[2])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 11 or ul.quiz_id == 111 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[2])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 12 or ul.quiz_id == 112 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[2])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 13 or ul.quiz_id == 113 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[2])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 14 or ul.quiz_id == 114 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[2])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 15 or ul.quiz_id == 115 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[3])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 16 or ul.quiz_id == 116 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[3])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 17 or ul.quiz_id == 117 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[3])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 18 or ul.quiz_id == 118 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[4])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 19 or ul.quiz_id == 119 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[4])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)
                        
                        elif ul.quiz_id == 20 or ul.quiz_id == 120 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[4])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 21 or ul.quiz_id == 121 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[5])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 22 or ul.quiz_id == 122 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[5])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 23 or ul.quiz_id == 123 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[5])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 24 or ul.quiz_id == 124 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[6])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 25 or ul.quiz_id == 125 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[6])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 26 or ul.quiz_id == 126 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[6])
                            list_vis_task.append(vis_task[2])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 27 or ul.quiz_id == 127 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[6])
                            list_vis_task.append(vis_task[4])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 28 or ul.quiz_id == 128 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[6])
                            list_vis_task.append(vis_task[5])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 29 or ul.quiz_id == 129 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[6])
                            list_vis_task.append(vis_task[6])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 30 or ul.quiz_id == 130 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[6])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 31 or ul.quiz_id == 131 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[7])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 32 or ul.quiz_id == 132 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[7])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 33 or ul.quiz_id == 133 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[7])
                            list_vis_task.append(vis_task[2])
                            list_status.append(ul.status)
                        
                        elif ul.quiz_id == 34 or ul.quiz_id == 134 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[7])
                            list_vis_task.append(vis_task[6])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 35 or ul.quiz_id == 135 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[8])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 36 or ul.quiz_id == 136 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[8])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 37 or ul.quiz_id == 137 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[8])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 38 or ul.quiz_id == 138 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[8])
                            list_vis_task.append(vis_task[6])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 39 or ul.quiz_id == 139 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[8])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 40 or ul.quiz_id == 140 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[8])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 41 or ul.quiz_id == 141 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[9])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 42 or ul.quiz_id == 142 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[9])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 43 or ul.quiz_id == 143 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[9])
                            list_vis_task.append(vis_task[2])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 44 or ul.quiz_id == 144 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[9])
                            list_vis_task.append(vis_task[4])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 45 or ul.quiz_id == 145 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[9])
                            list_vis_task.append(vis_task[5])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 46 or ul.quiz_id == 146 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[9])
                            list_vis_task.append(vis_task[6])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 47 or ul.quiz_id == 147 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[9])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 48 or ul.quiz_id == 148 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[10])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 49 or ul.quiz_id == 149 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[10])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 50 or ul.quiz_id == 150 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[10])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 51 or ul.quiz_id == 151 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[11])
                            list_vis_task.append(vis_task[1])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 52 or ul.quiz_id == 152 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[11])
                            list_vis_task.append(vis_task[7])
                            list_status.append(ul.status)

                        elif ul.quiz_id == 53 or ul.quiz_id == 153 :
                            list_user2.append(k)
                            list_quiz_id.append(ul.quiz_id)
                            list_vis_type.append(vis_type[11])
                            list_vis_task.append(vis_task[0])
                            list_status.append(ul.status)

                result_list2 = [['user_id','quiz_id','type','task','status']]

                for l2 in range(len(list_user2)):
                    arr1 = []
                    arr1.append(list_user2[l2])
                    arr1.append(list_quiz_id[l2])
                    arr1.append(list_vis_type[l2])
                    arr1.append(list_vis_task[l2])
                    arr1.append(list_status[l2])

                    result_list2.append(arr1)

                response = HttpResponse('text/csv')
                response['Content-Disposition'] = 'attachment; filename=k_vlat_resultdata.csv'
                writer = csv.writer(response)
                
                for row in result_list2:
                    writer.writerow(row)

                return response

    return render(request, "download.html")