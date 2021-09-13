from django.urls import path

from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('about/',views.about, name="about"),
    path('quiz/<int:quiz_id>/',views.quiz, name="quiz"),
    path('quiz_result/',views.quiz_result, name="quiz_result"),
    path('result/',views.result, name="result")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)