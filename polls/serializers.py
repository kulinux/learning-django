from rest_framework import serializers

from polls.models import Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question_text']