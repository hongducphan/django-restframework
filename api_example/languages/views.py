from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Programmer, Paradigm
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer
from rest_framework.response import Response
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response

class LanguageView(viewsets.ModelViewSet):
    def get(request):
        queryset = Language.objects.all()
        # serializer_class = LanguageSerializer(queryset, many='True', context={'request': request})
        
        # return TemplateResponse(request, 'base.html', {'data': serializer_class.data})
        return render_to_response('base.html', {'data': queryset})

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer