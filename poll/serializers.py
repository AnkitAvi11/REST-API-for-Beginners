from re import search
from .models import Question, Choice
from rest_framework import serializers

class ChoiceSerializer(serializers.ModelSerializer) : 
            
    class Meta : 
        model = Choice
        fields = [ 
            'id',
            'choice',
            'question',
            'created_on'
        ]

        read_only_fields = ['question']
        

class QuestionSerializer(serializers.ModelSerializer) : 

    choices = ChoiceSerializer(many=True, read_only=False)

    class Meta : 
        model = Question
        fields = [
            'id',
            'created_on',
            'question_title',
            'choices'
        ]
    
    #   overriding the create method
    def create(self, validated_data):
        mychoices = validated_data.pop('choices')

        question = Question.objects.create(**validated_data)

        for choice in mychoices : 
            Choice.objects.create(**choice, question=question)
        
        return question