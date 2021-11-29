from django.urls import path

from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('quiz2/', views.index2, name="index2"),
    path('about/',views.about, name="about"),
    path('quiz/<int:quiz_id>/',views.quiz, name="quiz"),
    path('quiz2/<int:quiz_id>/',views.quiz2, name="quiz2"),
    path('quiz/user/',views.user, name="user"),
    path('quiz/user/end1',views.user_end1, name="user_end1"),
    path('quiz/user/end2',views.user_end2, name="user_end2"),
    path('quiz_result/',views.quiz_result, name="quiz_result"),
    path('result/',views.result, name="result"),
    path('exportcsv/', views.exportcsv, name="exportcsv"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)