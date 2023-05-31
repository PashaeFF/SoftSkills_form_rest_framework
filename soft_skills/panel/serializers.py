from rest_framework import serializers

class InnerSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    answer_1 = serializers.CharField()
    answer_2 = serializers.CharField()
    answer_3 = serializers.CharField()
    answer_4 = serializers.CharField()
    answer_1_point = serializers.IntegerField()
    answer_2_point = serializers.IntegerField()
    answer_3_point = serializers.IntegerField()
    answer_4_point = serializers.IntegerField()

class QuestionSerializer(serializers.Serializer):
    question_1 = InnerSerializer()
    question_2 = InnerSerializer()
    question_3 = InnerSerializer()
    question_4 = InnerSerializer()
    question_5 = InnerSerializer()

class FormSerializer(serializers.Serializer):
    question_list_1 = QuestionSerializer()
    question_list_2 = QuestionSerializer()
    question_list_3 = QuestionSerializer()
    question_list_4 = QuestionSerializer()
    question_list_5 = QuestionSerializer()
    question_list_6 = QuestionSerializer()
    question_list_7 = QuestionSerializer()
    question_list_8 = QuestionSerializer()
    question_list_9 = QuestionSerializer()
    question_list_10 = QuestionSerializer()
    