from .models import Choice, Question

from rest_framework.decorators import api_view
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework.response import Response


@api_view(['GET','POST'])
def questions(request) : 
    if request.method == 'GET' : 
        questions = Question.objects.all()
        serialized_data = QuestionSerializer(questions, many=True).data
        return Response(serialized_data, status=200)
    else : 
        
        question = QuestionSerializer(data = request.data)
        if question.is_valid() : 
            question.save()
            return Response(question.data, status=200)
        else :
            return Response(question.errors, status=400)



@api_view(['GET'])
def choices(request) : 
    if request.method == 'GET' : 
        choices = Choice.objects.all()
        choiceserializer = ChoiceSerializer(choices, many=True)
        return Response(choiceserializer.data, status=200)
    