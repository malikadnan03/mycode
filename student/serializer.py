from rest_framework import serializers
from .models import Student, Subject, Marks

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']  # Only include 'id' and 'name' fields
        extra_kwargs = {'id': {'read_only': True}}  # Make 'id' read-only

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'
