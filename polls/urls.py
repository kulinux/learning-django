from django.urls import path
from rest_framework import routers, serializers, viewsets
from .models import Question

from . import views


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question,
        field = ['id', 'pub_date', 'question_text']


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='result'),
    path('<int:question_id>/vote/', views.results, name='vote'),
]