from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.db.models.functions import Coalesce
from .models import Student, Subject, Marks
from .serializers import StudentSerializer, SubjectSerializer, MarksSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

    def create(self, request, *args, **kwargs):
        try:
            student_roll = request.data.get('student', {}).get('roll_number')
            subject_name = request.data.get('subject', {}).get('name')
            total_marks = request.data.get('total_marks')

            if not student_roll or not subject_name or not total_marks:
                return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

            student, created = Student.objects.get_or_create(roll_number=student_roll)

            # Filter subjects based on name, choose the first one or create a new one
            subject = Subject.objects.filter(name=subject_name).first()
            if not subject:
                subject = Subject.objects.create(name=subject_name)

            marks_data = {
                'student': student.id,
                'subject': subject.id,
                'total_marks': total_marks,
            }

            serializer = MarksSerializer(data=marks_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print('Exception:', str(e))
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class JSONDataViewSet(viewsets.ViewSet):
    def list(self, request):
        students = Student.objects.all()
        subjects = Subject.objects.all()
        marks_data = []

        for student in students:
            marks = Marks.objects.filter(student=student)
            marks_data.append({
                'student': StudentSerializer(student).data,
                'marks': MarksSerializer(marks, many=True).data
            })

        return Response({'students': StudentSerializer(students, many=True).data,
                         'subjects': SubjectSerializer(subjects, many=True).data,
                         'marks_data': marks_data})

class RankViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            students = Student.objects.all()
            ranks = []

            sorted_students = sorted(students, key=lambda student: Marks.objects.filter(student=student).aggregate(
                total_marks=Coalesce(Sum('total_marks'), 0)
            )['total_marks'], reverse=True)

            prev_total_marks = None
            current_rank = 0 
            current_rank +1

            for student in sorted_students:
                total_marks = Marks.objects.filter(student=student).aggregate(
                    total_marks=Coalesce(Sum('total_marks'), 0)
                )['total_marks']

                if total_marks != prev_total_marks:
                    current_rank += 1

                ranks.append({'student_id': student.id, 'total_marks': total_marks, 'rank': current_rank})
                prev_total_marks = total_marks

            return Response({'rank_data': ranks})

        except Exception as e:
            print('Exception:', str(e))
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
