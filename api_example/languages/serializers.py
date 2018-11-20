from rest_framework import serializers
from .models import Language, Paradigm, Programmer

class LanguageSerializer(serializers.Serializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'paradigm')

class ParadigmSerializer(serializers.Serializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'name')

class ProgrammerSerializer(serializers.Serializer):
    class Meta:
        model = Programmer
        fields = ('id', 'name', 'languages')