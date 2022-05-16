from urllib import response
from django.http import HttpResponseRedirect, HttpResponse
from .models import Quiz, User, Answer
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
import csv


 
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
        upload_file = request.FILES['upload_file']
        file = upload_file.read().decode('utf-8').splitlines()
        
        reader = csv.reader(file)
        id_list = []
        for id in reader:
            id_list = id

        context = {'id_list' : id_list}
        return render(request, "download.html" ,context)
    
    return render(request, "download.html")