from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Question

# Create your views here.
from .serializers import QuestionSerializer


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse(
        "You're looking at the results of %s" % question_id)


def vote(request, question_id):
    return HttpResponse(
        "You're voting on question %s" % question_id)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def mono(request):
    return Response({"mono": "true"})


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
