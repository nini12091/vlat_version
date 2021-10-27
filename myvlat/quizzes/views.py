from django.http import HttpResponseRedirect
from .models import Quiz, User, Answer, Result
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
from django.urls import reverse



def index(request):
    # Session 생성
    request.session.create()
    userID = str(request.session.session_key)
    today = str(datetime.now().strftime("%I:%M%p on %B %d, %Y"))
    request.session['userID'] = userID
    request.session['statedate'] = today

    # Session DB 저장
    user = User()
    user.user_id = userID
    user.statedate = today
    user.save()

    return render(request, "index.html")

def quiz(request, quiz_id):
    if quiz_id <= 5:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz.html", context)

    elif 5 < quiz_id <= 9:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz2.html", context)

    elif 9 < quiz_id <= 14:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz3.html", context)
    
    elif 14 < quiz_id <= 17:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz4.html", context)
    
    elif 17 < quiz_id <= 20:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz5.html", context)

    elif 20 < quiz_id <= 23:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz6.html", context)

    elif 23 < quiz_id <= 30:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz7.html", context)

    elif 30 < quiz_id <= 34:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz8.html", context)

    elif 34 < quiz_id <= 40:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz9.html", context)

    elif 40 < quiz_id <= 47:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz10.html", context)

    elif 47 < quiz_id <= 50:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz11.html", context)

    elif 50 < quiz_id <= 54:
        if request.method == 'POST':
            quiz = Quiz.objects.get(pk=request.session['quizId'])
            answer = Answer()
            answer.choice_id = str(str(quiz_id) + request.session.session_key)
            answer.user_id = str(request.session.session_key)
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
            return render(request, "quiz12.html", context)
    else:
        return render(request, "user.html")

def user(request):
    if request.method == "POST":
        user = User()
        user.user_age = request.POST.get('user_age','')
        user.user_education = request.POST.get('user_education','')
        user.save()
    else:
        return render(request, "user.html")

def user_end1(request):
    if request.method == "POST":
        user = User()
        user.purpose = request.POST.get('purpose','')
        user.save()

    return render(request, "user_end1.html")

def user_end2(request):
    if request.method == "POST":
        user = User()
        user.user_major = request.POST.get('user_major','')
        user.purpose = request.POST.get('purpose','')
        user.save()
    return render(request, "user_end2.html")

def quiz_result(request):
    userID = str(request.session.session_key)
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
